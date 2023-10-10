from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.LoginUser.as_view(), name='login'),
    path('register', views.RegisterUser.as_view(), name='register'),
    path('logout', views.logout_user, name='logout'),
    path('actors/', views.ListActor.as_view(), name='actors'),
    path('actors/<int:pk>', views.DetailActor.as_view(), name='actor_detail'),
    path('directors/<int:pk>', views.DetailDirector.as_view(), name='director_detail'),
    path('directors/', views.ListDirector.as_view(), name='directors'),
    path('search/', views.Search.as_view(), name='search'),
    path('movies/<int:pk>', views.DetailMovie.as_view(), name='movie_detail'),
    path('movies/', views.ListMovie.as_view(), name='movies'),
    path('api/v1/director/', views.DirectorAPIList.as_view()),
    path('api/v1/director/detail/<int:pk>/', views.DirectorAPIDetail.as_view()),
    path('api/v1/actor/', views.DirectorAPIList.as_view()),
    path('api/v1/actor/detail/<int:pk>/', views.DirectorAPIDetail.as_view()),
    path('', views.glavnaya, name='main'),
]
