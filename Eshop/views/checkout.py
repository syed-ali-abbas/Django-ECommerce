from django.views import View
from django.shortcuts import render, redirect
from Eshop.models.Product import Product
from Eshop.models.order import Order
from Eshop.models.Customer import Customer
# from Eshop.middlewares.auth import auth_middleware
# from django.utils.decorators import method_decorator


class Checkout(View):
    # @method_decorator(auth_middleware)
    def post(self, request):
        address = request.POST.get('address')
        mobile_number = request.POST.get('mobile_number')
        customer = request.session.get('customer_id')
        cart = request.session.get('cart')
        products = Product.get_product_by_id(list(cart.keys()))
        for product in products:
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          mobile_number=mobile_number,
                          quantity=cart.get(str(product.id)),
                          )
            order.placeOrder()
        request.session['cart']={}

        return redirect('cart')
