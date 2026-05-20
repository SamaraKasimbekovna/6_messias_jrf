import random

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from .models import ConfirmCode
from .serializers import (
    UserRegisterSerializer,
    UserAuthSerializer,
    ConfirmSerializer
)

class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.create_user(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
            is_active=False
        )

        code = str(random.randint(100000, 999999))

        ConfirmCode.objects.create(
            user=user,
            code=code
        )

        print({'user_id': user.id, 'code': code})

        return Response({
            'user_id': user.id,
            'code': code
        }, status=status.HTTP_201_CREATED)

class ConfirmAPIView(APIView):
    def post(self, request):
        serializer = ConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            confirm = ConfirmCode.objects.get(
                user_id=serializer.validated_data['user_id'],
                code=serializer.validated_data['code']
            )
        except ConfirmCode.DoesNotExist:
            return Response(
                {'error': 'Invalid code'},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = confirm.user
        user.is_active = True
        user.save()

        confirm.delete()

        return Response({'status': 'confirmed'})

class AuthorizationAPIView(APIView):
    def post(self, request):
        serializer = UserAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )

        if not user:
            return Response(
                {'error': 'Unauthorized'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        token, _ = Token.objects.get_or_create(user=user)

        return Response({'key': token.key})