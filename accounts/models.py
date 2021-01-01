from django.db import models

# Create your models here.

class massage_request(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.ImageField(max_length=10)
    message = models.CharField(max_length=500)
    
