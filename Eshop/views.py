from django.shortcuts import render, redirect
from .models.Product import Product
from .models.Category import Category
from django.http import HttpResponse
from .models.Customer import Customer


# Create your views here.

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


def register(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        post_data = request.POST
        first_name = post_data.get('firstname')
        last_name = post_data.get('lastname')
        phone = post_data.get('phone')
        password = post_data.get('password')
        email = post_data.get('email')

        obj_val = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        obj = Customer(first_name=first_name, last_name=last_name, phone=phone, password=password, email=email)
        error_msg = None
        if not first_name:
            error_msg = 'First Name is required'
        elif len(first_name) < 5:
            error_msg = 'First Name length should be smaller than 5'
        elif not last_name:
            error_msg = 'Last Name is required'
        elif len(last_name) < 5:
            error_msg = 'Last Name length should be smaller than 5'
        elif not password:
            error_msg = 'Password Required'
        elif len(password) < 8:
            error_msg = 'Password Characters Should be greater than 8'
        elif not phone:
            error_msg = 'Phone Number required'
        elif len(phone) < 15:
            error_msg = 'Phone Number length 15 digits required'
        elif not email:
            error_msg = 'Email Required'
        elif len(email) < 5:
            error_msg = 'Email Incorrect'
        elif obj.if_exists():
            error_msg='Email Address Already Exists'
        if not error_msg:
            obj.register()
            return redirect('home')
        else:
            data = {
                'error': error_msg,
                'obj_data': obj_val
            }
            return render(request, 'signup.html', data)
