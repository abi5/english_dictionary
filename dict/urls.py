from django.urls import path, include
from dict import views

urlpatterns = [
    path('',views.login_page,name = 'login'),
    path('register',views.register,name = 'register'),
    path('mainpage',views.mainpage,name = 'mainpage'),
    path('logout',views.logout,name = 'logout'),
]
