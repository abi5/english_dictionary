from django.urls import path, include
from dict import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('register',views.register,name = 'register'),
    path('mainpage',views.mainpage,name = 'mainpage'),
]
