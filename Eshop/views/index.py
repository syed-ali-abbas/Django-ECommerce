from django.shortcuts import render, redirect
from Eshop.models.Product import Product
from Eshop.models.Category import Category






def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryid = request.GET.get('category')
    if categoryid:
        products = Product.get_all_ProductsByCategory(categoryid)
    else:
        products = Product.get_all_products()

    data_dictionary = {
        'products': products,
        'category': categories
    }
    return render(request, 'home.html', data_dictionary)














