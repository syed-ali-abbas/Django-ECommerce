from django.views import View
from django.shortcuts import render
from Eshop.models.order import Order
# from Eshop.middlewares.auth import auth_middleware
# from django.utils.decorators import method_decorator


class orders(View):
    # @method_decorator(auth_middleware)
    def get(self, request):
        customer = request.session.get('customer_id')
        orders = Order.get_orders_by_customer(customer)
        return render(request, 'Orders.html',{'orders':orders})
