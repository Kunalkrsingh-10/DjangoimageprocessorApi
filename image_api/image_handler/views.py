from django.shortcuts import render
import uuid
import csv
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .tasks import process_images

@api_view(['POST'])
def upload_csv(request):
    if 'file' not in request.FILES:
        return Response({'error': 'No file part'}, status=400)
    
    csv_file = request.FILES['file']
    decoded_file = csv_file.read().decode('utf-8').splitlines()
    reader = csv.reader(decoded_file)

    for row in reader:
        product_name = row[1]
        input_image_urls = row[2]
        request_id = str(uuid.uuid4())
        product = Product.objects.create(
            product_name=product_name,
            input_image_urls=input_image_urls,
            request_id=request_id
        )
        process_images.delay(product.id)

    return Response({'request_id': request_id}, status=201)

@api_view(['GET'])
def check_status(request, request_id):
    try:
        product = Product.objects.get(request_id=request_id)
        return Response({
            'status': product.status,
            'input_image_urls': product.input_image_urls,
            'output_image_urls': product.output_image_urls,
        })
    except Product.DoesNotExist:
        return Response({'error': 'Invalid request ID'}, status=404)

