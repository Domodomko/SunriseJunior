from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField('Name', max_length=100, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class SubCategory(models.Model):
    name = models.CharField('Name', max_length=100, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'


class Product(models.Model):
    name = models.CharField('Name', max_length=100, default='')
    description = models.CharField('Description', max_length=500, default='')
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'