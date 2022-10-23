from django.db import models
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=100)
    year=models.IntegerField(blank=True)
    budget = models.IntegerField(validators=[MinValueValidator(1)])
    director = models.CharField(max_length=70)
    image = models.FileField(upload_to='my_gallery')
    description=models.CharField(max_length=10000)
    def __str__(self):
        return f'{self.title} {self.budget}'