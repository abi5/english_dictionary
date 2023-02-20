from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from English_Dictionary import settings
from django.core.mail import send_mail

from django.contrib.auth import authenticate, login, logout
# Create your views here.

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for' + user)

            return redirect('/')

    context = {'form': form}
    return render(request, 'Dict/register.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('mainpage')
        else:
            messages.info(request, 'Username or Password  is Incorrect')

    return render(request, 'Dict/login.html')


def mainpage(request):
    subject = 'welcome to GFG world'
    message = f'Hi thank you for registering in geeksforgeeks.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['keerthangowda8318@gmail.com',]
    send_mail(subject, message, email_from, recipient_list)
    return render(request, 'Dict/mainpage.html')

def logout(request):
    return redirect('/')