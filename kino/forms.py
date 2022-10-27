from django import forms
from .models import Movie
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

from django.forms import ValidationError


class RegisterUserForm(UserCreationForm):
    #Форма регистрации пользователя
    username=forms.CharField(label='Логин',widget=forms.TextInput(attrs={'class':'field_register'}))  #widget=forms.TextInput(attrs={'class':'какой-то класс css'}
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'field_register'}),error_messages={
        "invalid":"Введите email в нужном формате somesymbols@whatever.com"
    })
    password1 = forms.CharField(label='Пароль',widget=forms.TextInput(attrs={'class':'field_register'}))
    password2 = forms.CharField(label='Повтор пароля',widget=forms.TextInput(attrs={'class':'field_register'}))


    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label = 'Логин')
    password = forms.CharField(label = 'Пароль')
