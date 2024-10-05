from django import forms
from django.contrib.auth.forms import AuthenticationForm   

from users.models import User

class UserLoginForm(AuthenticationForm):

    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'autofocus': True,
                                      'placeholder': 'Введите логин'}),
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",
                                    'class': 'form-control',
                                    'placeholder': 'Введите пароль'}),
    )
    class Meta:
        model = User
        fields = ['username', 'password']