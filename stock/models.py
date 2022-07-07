from django.db import models

# Create your models here.


class Product(models.Model):
    product = models.CharField(max_length=100,null=True)
    price = models.CharField(max_length=100,null=True)
    reviews = models.CharField(max_length=40,null=True)
    rates =models.CharField(max_length=100,null=True)

