# Generated by Django 4.1.7 on 2023-10-08 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kino', '0026_alter_movie_actors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(default=None, null=True, to='kino.actor'),
        ),
    ]
