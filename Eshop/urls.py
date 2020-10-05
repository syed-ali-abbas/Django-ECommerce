from django.urls import path
from .views import index,login, signup
# from .views.login import Login, Logout
# from .views.signup import SignUp
from .views.cart import cart
from .views.checkout import Checkout

urlpatterns = [
    path('', index.Index.as_view(), name = 'home'),
    path('signup',signup.SignUp.as_view()),
    path('signin',login.Login.as_view(), name = 'login'),
    path('signout',login.Logout, name = 'logout'),
    path('cart',cart.as_view(),name='cart'),
    path('check-out', Checkout.as_view(), name='check-out')
]