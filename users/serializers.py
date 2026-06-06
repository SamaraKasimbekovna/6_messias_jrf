from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(
    TokenObtainPairSerializer
):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["birthdate"] = (
            user.birthdate.isoformat()
            if user.birthdate
            else None
        )

        return token


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "password",
            "phone_number",
            "birthdate"
        ]
        # fields = ["email", "password", "phone_number"]

    def validate_email(self, value):

        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("Пользователь уже существует")

        return value

    def create(self, validated_data):

        password = validated_data.pop("password")

        user = CustomUser.objects.create_user(
            password=password,
            **validated_data
        )

        return user


class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()

    password = serializers.CharField(write_only=True)

    def validate(self, attrs):

        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(
            username=email,
            password=password
        )

        if not user:
            raise serializers.ValidationError("Неверный email или пароль")

        attrs["user"] = user

        return attrs