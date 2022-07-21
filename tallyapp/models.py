from ast import alias
from django.db import models

# Create your models here.

class stock_group(models.Model):
    stock_group_name=models.CharField(max_length=100)
    alias=models.CharField(max_length=10)
    under=models.CharField(max_length=100)
    should_quantity_of_items_be_added=models.CharField(max_length=5)

class stock_category(models.Model):
    stock_category_name=models.CharField(max_length=100)
    alias=models.CharField(max_length=10)
    under=models.CharField(max_length=100)

class location(models.Model):
    location_name=models.CharField(max_length=100)
    alias=models.CharField(max_length=10)
    under=models.CharField(max_length=100)

# class companypricelevel(models.Model):
#     price_level_name=models.CharField(max_length=100)

class unit(models.Model):
