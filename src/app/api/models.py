from django.db import models
import uuid
from django.urls.base import reverse


class Product(models.Model):
    barcode = models.CharField(max_length=20, null=True)
    brand = models.CharField(max_length=100, null=True)
    sub_brand = models.CharField(max_length=100, blank=True, null=True)
    manufactured_by = models.CharField(max_length=200, null=True)
    product_name = models.CharField(max_length=200, null=True)
    weight = models.FloatField(null=True)
    variant = models.CharField(max_length=100, blank=True, null=True)
    net_content = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    parent_category = models.CharField(max_length=100, null=True)
    child_category = models.CharField(max_length=100, null=True)
    sub_child_category = models.CharField(max_length=100, blank=True, null=True)
    images_paths = models.CharField(max_length=3000, blank=True, null=True) # Comma separated paths
    description = models.TextField(max_length=3000, blank=True, null=True)
    quantity = models.IntegerField(null=True, blank=True)
    mrp = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.product_name


class Database(models.Model):
    barcode = models.CharField(max_length=20, null=True)
    brand = models.CharField(max_length=100, null=True)
    sub_brand = models.CharField(max_length=100, blank=True, null=True)
    manufactured_by = models.CharField(max_length=200, null=True)
    product_name = models.CharField(max_length=200, null=True)
    weight = models.FloatField(null=True)
    variant = models.CharField(max_length=100, blank=True, null=True)
    net_content = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    parent_category = models.CharField(max_length=100,null=True)
    child_category = models.CharField(max_length=100,null=True)
    sub_child_category = models.CharField(max_length=100, blank=True, null=True)
    images_paths = models.CharField(max_length=3000, blank=True, null=True) # Comma separated paths
    description = models.TextField(max_length=3000, blank=True, null=True)
    quantity = models.IntegerField(null=True, blank=True)
    promotion_on_the_pack = models.CharField(max_length=100, blank=True, null=True)
    type_of_packaging = models.CharField(max_length=100, blank=True, null=True)
    mrp = models.CharField(max_length=100, blank=True, null=True)
