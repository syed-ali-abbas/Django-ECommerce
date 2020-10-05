from django.views import View
from django.shortcuts import render
from Eshop.models.Product import Product


class cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_product_by_id(ids)
        return render(request,'cart.html', {'products':products})
