from django.shortcuts import render

from users.forms import UserLoginForm
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse

def login(request):
    
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
            

    contex={
        'title':'Авторизация',
        'form':form
    }
    return render(request, 'users/login.html', contex)


def registration(request):
    contex = {
        'title': 'Регистрация'
    }
    return render(request, 'users/registration.html', contex)


def profile(request):
    contex = {
        'title': 'Профиль'
    }
    return render(request, 'users/profile.html', contex)


def logout(request):
    contex = {
        'title': 'Выход'
    }
    return render(request, 'users/logout.html', contex)
