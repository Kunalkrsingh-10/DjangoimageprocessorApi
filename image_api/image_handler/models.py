from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    input_image_urls = models.TextField()  
    output_image_urls = models.TextField(null=True, blank=True)  
    request_id = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=50, default='Pending') 
    created_at = models.DateTimeField(auto_now_add=True)
