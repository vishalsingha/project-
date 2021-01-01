from django.db import models

# Create your models here.



class doctor(models.Model):
    pic = models.ImageField(upload_to='pics')


class tomato_plant(models.Model):
    disease_name = models.CharField(max_length=100)
    disease_treatments1 = models.TextField(max_length=3000)
    disease_treatments2 = models.TextField(max_length=3000)
    disease_treatments3 = models.TextField(max_length=3000)
    disease_treatments4 = models.TextField(max_length=3000)
    disease_control1 = models.TextField(max_length=3000)
    disease_control2 = models.TextField(max_length=3000)
    disease_control3 = models.TextField(max_length=3000)
    disease_control4 = models.TextField(max_length=3000)


class apple_plant(models.Model):
    disease_name = models.CharField(max_length=100)
    disease_treatments = models.TextField(max_length=3000)
    disease_control = models.TextField(max_length=3000)

class grapes_plant(models.Model):
    disease_name = models.CharField(max_length=100)
    disease_treatments = models.TextField(max_length=3000)
    disease_control = models.TextField(max_length=3000)

class corn_plant(models.Model):
    disease_name = models.CharField(max_length=100)
    disease_treatments = models.TextField(max_length=3000)
    disease_control = models.TextField(max_length=3000)

