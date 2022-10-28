from django.db import models
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from .validators import validate_file_extension


# Create your models here.
class Actor(models.Model):
    '''Модель для описания актера'''
    first_name = models.CharField(max_length=40)
    second_name = models.CharField(max_length=40)
    date_of_birth = models.DateField()
    height = models.FloatField(
        validators=[MaxValueValidator(2.30), MinValueValidator(1.30)])  # Ограничиваем рост актера
    image = models.FileField(upload_to='directors', null=True)
    place_of_birth = models.CharField(max_length=200, null=True, default=None)
    interesting_fact = models.CharField(max_length=1000, null=True, default=None, blank=True)
    numbers_of_oscar = models.IntegerField(validators=[MinValueValidator(0)], null=True, default=None)

    def __str__(self):
        return f'{self.first_name} {self.second_name}'


class Director(models.Model):
    '''Модель для описания режиссера'''
    first_name = models.CharField(max_length=40)
    second_name = models.CharField(max_length=40)
    date_of_birth = models.DateField()
    height = models.FloatField(
        validators=[MaxValueValidator(2.30), MinValueValidator(1.30)])  # Ограничиваем рост режиссера
    genres = models.CharField(max_length=1000)  # В последствии добавить отдельную модель для жанра
    image = models.FileField(upload_to='actors',null=True)
    place_of_birth=models.CharField(max_length=200,null=True,default=None)
    interesting_fact=models.CharField(max_length=1000,null=True,default=None,blank=True)
    numbers_of_oscar=models.IntegerField(validators=[MinValueValidator(0)],null=True,default=None)

    def __str__(self):
        return f'{self.first_name} {self.second_name}'  # Для отображения в админ панели


class Movie(models.Model):
    
    title = models.CharField(max_length=100)
    year = models.IntegerField(blank=True)
    budget = models.IntegerField(validators=[MinValueValidator(1)])
    director = models.ForeignKey(Director,on_delete=models.CASCADE,null=True,blank=True,default=None)
    image = models.FileField(upload_to='my_gallery')
    description = models.CharField(max_length=10000)
    actors=models.ManyToManyField(Actor)

    def __str__(self):
        return f'{self.title} {self.budget}'  # Для отображения в админ панели

