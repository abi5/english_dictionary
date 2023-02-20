from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages

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
    return render(request, 'Dict/mainpage.html')

def logout(request):
    return redirect('/')