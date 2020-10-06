from django.urls import path
from .views import index, login, signup, Orders
from .views.cart import cart
from .views.checkout import Checkout
from Eshop.middlewares.auth import auth_middleware


urlpatterns = [
    path('', index.Index.as_view(), name='home'),
    path('signup', signup.SignUp.as_view()),
    path('signin', login.Login.as_view(), name='login'),
    path('signout', login.Logout, name='logout'),
    path('cart', auth_middleware(cart.as_view()), name='cart'),
    path('check-out', auth_middleware(Checkout.as_view()), name='check-out'),
    path('orders',auth_middleware(Orders.orders.as_view()) , name='orders')

]
