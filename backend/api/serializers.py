from rest_framework import serializers
from .models import Book
from django.contrib.auth.models import User

class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",  # Исправлено с "user" на "username"
            "email",
            "password",
            "first_name",
            "last_name",
        )
        # Скрываем пароль в ответах (write_only), чтобы его нельзя было прочитать
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"required": True} # По желанию: делаем email обязательным
        }

    def create(self, validated_data):
        # Используем специальный метод create_user для хэширования пароля
        return User.objects.create_user(**validated_data)