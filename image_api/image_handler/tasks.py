import requests
from PIL import Image
from io import BytesIO
from celery import shared_task
from .models import Product
import json

@shared_task
def process_images(product_id):
    product = Product.objects.get(id=product_id)
    input_urls = product.input_image_urls.split(',')
    output_urls = []
    for url in input_urls:
        response = requests.get(url.strip())
        img = Image.open(BytesIO(response.content))
        output = BytesIO()
        img.save(output, format='JPEG', quality=50)
        output_urls.append(url.strip())

    
    product.output_image_urls = ','.join(output_urls)
    product.status = 'Completed'
    product.save()

    
    webhook_url = "https://webhook.site/your-webhook-url"  
    data = {
        'request_id': product.request_id,
        'status': product.status,
    }

    
    requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
