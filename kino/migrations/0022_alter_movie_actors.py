# Generated by Django 4.1.1 on 2022-10-28 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kino', '0021_actor_movie_actors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(to='kino.actor'),
        ),
    ]
