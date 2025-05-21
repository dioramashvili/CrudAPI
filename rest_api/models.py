from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Category Name')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Product Name')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Price')
    stock = models.IntegerField(null=False, blank=False, verbose_name='Stock')
    category = models.ManyToManyField('Category', related_name='Product', verbose_name='Category')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
