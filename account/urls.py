from django.urls import path
from .views import *
urlpatterns = [

    path('login',loginpage,name = "login"),
    path('registeruser',registeruser,name = "registeruser"),

    path('logout/', logout_page, name='logout'),
    
]
