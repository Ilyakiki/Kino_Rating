
from django.urls import path,include
from . import views
urlpatterns = [
    path('movies/<int:pk>',views.DetailMovie.as_view(),name='movie.detail'),
    path('movies/',views.ListMovie.as_view(),name='movies'),
    path('',views.glavnaya,name='main'),
]
