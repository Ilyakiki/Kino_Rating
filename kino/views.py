from django.shortcuts import render, redirect
import requests
from rest_framework import generics
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterUserForm, LoginUserForm
from .models import Movie, Director, Actor
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from kino.serializers import *
from kino.permitions import *
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.contrib.auth import logout, login


# Create your views here.

def glavnaya(request):
    return render(request, 'kino/main.html')


class ListMovie(ListView):
    '''Список Фильмов'''
    paginate_by = 3  # Пагинация
    template_name = 'kino/list_movie.html'
    model = Movie
    context_object_name = 'Movies'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset


class ListDirector(ListView):
    '''Список Режиссеров'''
    paginate_by = 3  # Пагинация
    template_name = 'kino/list_directors.html'
    model = Director
    context_object_name = 'Directors'

    def get_queryset(self):
        queryset = super().get_queryset()
        # filtered_qs=queryset.filter(rating__gt=4)
        return queryset


class ListActor(ListView):
    '''Список Актеров'''
    paginate_by = 5  # Пагинация
    template_name = 'kino/list_actors.html'
    model = Actor
    context_object_name = 'Actors'

    def get_queryset(self):
        queryset = super().get_queryset()
        # filtered_qs=queryset.filter(rating__gt=4)
        return queryset


class DetailMovie(DetailView):
    '''Детальное представление фильма'''
    template_name = 'kino/detail_view.html'
    model = Movie

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DetailDirector(DetailView):
    '''Детальное представление режиссера'''
    template_name = 'kino/detail_director.html'
    model = Director


class DetailActor(DetailView):
    '''Детальное представление актера'''
    template_name = 'kino/detail_actor.html'
    model = Actor


class RegisterUser(CreateView):
    '''регистрация'''
    form_class = RegisterUserForm
    template_name = 'kino/register.html'
    success_url = 'kino/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect('/')


class LoginUser(LoginView):
    '''вход в аккаунт'''
    form_class = LoginUserForm
    template_name = 'kino/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse('main')


def logout_user(request):
    '''выход из аккаунт'''
    logout(request)
    return HttpResponseRedirect('login')


class Search(ListView):
    '''Поиск Фильмов'''
    template_name = 'kino/list_movie.html'
    model = Movie

    def get_queryset(self):
        queryset = super().get_queryset()
        p = self.request.GET.get(
            'q').lower().title()  # Для того,чтобы в поисковой строке можно было вводить название в любом регистре
        filtered_qs = queryset.filter(title__icontains=p)
        return filtered_qs

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = f'{self.request.GET.get("q")}&'
        return context


class DirectorAPIList(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = (IsAdminOrReadOnly,)


