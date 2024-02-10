from django.db import models

class Product(models.Model):
    barcode = models.CharField(max_length=20)
    brand = models.CharField(max_length=100)
    sub_brand = models.CharField(max_length=100, blank=True, null=True)
    manufactured_by = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    weight = models.FloatField()
    variant = models.CharField(max_length=100, blank=True, null=True)
    net_content = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    parent_category = models.CharField(max_length=100)
    child_category = models.CharField(max_length=100)
    sub_child_category = models.CharField(max_length=100, blank=True, null=True)
    images_paths = models.CharField(max_length=3000, blank=True, null=True) # Comma separated paths
    description = models.TextField(max_length=3000, blank=True, null=True)
    quantity = models.IntegerField(null=True, blank=True)
    mrp = models.CharField(max_length=100, blank=True, null=True)

    def _str_(self):
        return self.product_name


class Database(models.Model):
    barcode = models.CharField(max_length=20)
    brand = models.CharField(max_length=100)
    sub_brand = models.CharField(max_length=100, blank=True, null=True)
    manufactured_by = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    weight = models.FloatField()
    variant = models.CharField(max_length=100, blank=True, null=True)
    net_content = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    parent_category = models.CharField(max_length=100)
    child_category = models.CharField(max_length=100)
    sub_child_category = models.CharField(max_length=100, blank=True, null=True)
    images_paths = models.CharField(max_length=3000, blank=True, null=True) # Comma separated paths
    description = models.TextField(max_length=3000, blank=True, null=True)
    quantity = models.IntegerField(null=True, blank=True)
    promotion_on_the_pack = models.CharField(max_length=100, blank=True, null=True)
    type_of_packaging = models.CharField(max_length=100, blank=True, null=True)
    mrp = models.CharField(max_length=100, blank=True, null=True)