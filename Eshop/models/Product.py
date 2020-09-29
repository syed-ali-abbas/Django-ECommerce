from django.db import models
from .Category import Category


class Product(models.Model):
    name = models.CharField(max_length=850)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='')
    category_ID = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    Image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products():
        return Product.objects.all()


    @staticmethod
    def get_all_ProductsByCategory(category_ID_id):
        if category_ID_id:
            return Product.objects.filter(category_ID=category_ID_id)
        else:
            return Product.get_all_products()
