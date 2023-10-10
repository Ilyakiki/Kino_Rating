import io
from rest_framework import serializers
from .models import *


# Сериализатор для модели Director
class DirectorSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Director
        fields = "__all__"


# Сериализатор для модели Actor
class ActorSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Actor
        fields = "__all__"


# Сериализатор для модели Movie
class MovieSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Movie
        fields = "__all__"
