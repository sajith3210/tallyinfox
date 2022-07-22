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

class companypricelevel(models.Model):
    price_level_name=models.CharField(max_length=100)

class unit(models.Model):
    type=models.CharField(max_length=50,null=True,blank=True)
    symbol=models.CharField(max_length=50,null=True,blank=True)
    formal_name=models.CharField(max_length=50,null=True,blank=True)
    number_of_decimal_places=models.IntegerField(null=True,blank=True)
    first_unit=models.CharField(max_length=50)
    conversion=models.IntegerField(null=True,blank=True)
    second_unit=models.CharField(max_length=50,null=True,blank=True)

