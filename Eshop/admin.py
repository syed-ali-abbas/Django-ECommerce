from django.contrib import admin
from .models.Product import Product
from .models.Category import Category
from .models.Customer import Customer


# Register your models here.

class AdminProductTab(admin.ModelAdmin):
    list_display = ['name', 'price', 'category_ID']


class AdminCategoryTab(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Product, AdminProductTab)
admin.site.register(Category, AdminCategoryTab)
admin.site.register(Customer)
