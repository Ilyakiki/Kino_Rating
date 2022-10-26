
from django.urls import path,include
from . import views
urlpatterns = [
    path('directors/<int:pk>',views.DetailDirector.as_view(),name='director_detail'),
    path('directors/',views.ListDirector.as_view(),name='directors'),
    path('movies/<int:pk>',views.DetailMovie.as_view(),name='movie_detail'),
    path('movies/',views.ListMovie.as_view(),name='movies'),
    path('',views.glavnaya,name='main'),
]

