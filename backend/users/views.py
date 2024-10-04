from django.shortcuts import render

def login(request):
    contex={
        'title':'Авторизация',
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
