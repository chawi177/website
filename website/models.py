from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    image_relative_url = models.CharField(max_length=50, null=True, blank=True)