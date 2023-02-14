from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'Dict/home.html')

def register(request):
    return render(request, 'Dict/registration.html')

def mainpage(request):
    return render(request, 'Dict/mainpage.html')