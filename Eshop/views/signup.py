from django.shortcuts import render, redirect

from Eshop.models.Customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View




class SignUp(View):
    def get(self, request):
        return render(request, 'signup.html')

    def validate(self, obj):
        error_msg = None
        if not obj.first_name:
            error_msg = 'First Name is required'
        elif len(obj.first_name) < 5:
            error_msg = 'First Name length should be smaller than 5'
        elif not obj.last_name:
            error_msg = 'Last Name is required'
        elif len(obj.last_name) < 5:
            error_msg = 'Last Name length should be smaller than 5'
        elif not obj.password:
            error_msg = 'Password Required'
        elif len(obj.password) < 8:
            error_msg = 'Password Characters Should be greater than 8'
        elif not obj.phone:
            error_msg = 'Phone Number required'
        elif len(obj.phone) < 15:
            error_msg = 'Phone Number length 15 digits required'
        elif not obj.email:
            error_msg = 'Email Required'
        elif len(obj.email) < 5:
            error_msg = 'Email Incorrect'
        elif obj.if_exists():
            error_msg = 'Email Address Already Exists'
        return error_msg



    def post(self, request):
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
        error_msg = self.validate(obj)
        if not error_msg:
            obj.password = make_password(obj.password)
            obj.register()
            return redirect('home')
        else:
            data = {
                'error': error_msg,
                'obj_data': obj_val
            }
            return render(request, 'signup.html', data)