from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterUserForm,LoginUserForm
from django.views import View
from .models import Movie,Director
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView
import requests
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.contrib.auth import logout,login
# Create your views here.

def glavnaya(request):
    return render(request,'kino/main.html')


class ListMovie(ListView):
    paginate_by = 3  # Пагинация
    template_name = 'kino/list_movie.html'
    model = Movie
    context_object_name = 'Movies'

    def get_queryset(self):
        queryset = super().get_queryset()
        # filtered_qs=queryset.filter(rating__gt=4)
        return queryset


class DetailMovie(DetailView):
    template_name = 'kino/detail_view.html'
    model=Movie

    def get_absolute_url(self):
        return reverse('movie_detail',kwargs={'pk':self.pk_url_kwarg})

class DetailDirector(DetailView):
    template_name = 'kino/detail_director.html'
    model=Director
class ListDirector(ListView):
    paginate_by = 3  # Пагинация
    template_name = 'kino/list_directors.html'
    model = Director
    context_object_name = 'Directors'

    def get_queryset(self):
        queryset = super().get_queryset()
        # filtered_qs=queryset.filter(rating__gt=4)
        return queryset

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'kino/register.html'
    success_url = 'kino/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user=form.save()
        login(self.request,user)
        return HttpResponseRedirect('/')

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'kino/login.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse('main')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('login')