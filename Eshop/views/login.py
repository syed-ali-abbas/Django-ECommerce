from Eshop.models.Customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from django.shortcuts import render, redirect



class Login(View):
    def get(self, request):
        return render(request, 'signin.html')

    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_msg = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                # request.session['email'] = customer.email
                return redirect('home')
            else:
                error_msg = 'Email or Password incorrect..'

            pass
        else:
            error_msg = 'Email or Password incorrect..'
        return render(request, 'signin.html', {'error': error_msg})


def Logout(request):
    request.session.clear()
    return redirect('login')