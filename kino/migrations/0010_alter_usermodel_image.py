# Generated by Django 4.1.1 on 2022-10-27 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kino', '0009_usermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='image',
            field=models.FileField(default=None, null=True, upload_to='avatars'),
        ),
    ]