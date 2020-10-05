from django.shortcuts import render, redirect
from Eshop.models.Product import Product
from Eshop.models.Category import Category
from django.views import View


class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        return redirect('home')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
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
