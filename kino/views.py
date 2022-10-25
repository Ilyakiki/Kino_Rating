from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponseRedirect
#from .forms import FeedbackForm, RegisterUserForm,LoginUserForm
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
