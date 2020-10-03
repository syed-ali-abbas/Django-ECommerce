from django.urls import path
from .views import index,login, signup
# from .views.login import Login
# from .views.signup import SignUp

urlpatterns = [
    path('', index.index, name = 'home'),
    path('signup',signup.SignUp.as_view()),
    path('signin',login.Login.as_view())
]