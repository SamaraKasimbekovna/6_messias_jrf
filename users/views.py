from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    UserRegisterSerializer,
    UserAuthSerializer,
    ConfirmSerializer
)

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.authtoken.models import Token

from .models import ConfirmCode

import random


@api_view(['POST'])
def registration_api_view(request):
    serializer = UserRegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data['username']
    password = serializer.validated_data['password']

    user = User.objects.create_user(
        username=username,
        password=password,
        is_active=False
    )

    code = str(random.randint(100000, 999999))

    ConfirmCode.objects.create(
        user=user,
        code=code
    )

    result = {
        'user_id': user.id,
        'code': code
    }

    print(result)

    return Response(
        status=status.HTTP_201_CREATED,
        data={
            'user_id': user.id,
            'code': code
        }
    )


@api_view(['POST'])
def confirm_api_view(request):
    serializer = ConfirmSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user_id = serializer.validated_data['user_id']
    code = serializer.validated_data['code']

    try:
        confirm = ConfirmCode.objects.get(
            user_id=user_id,
            code=code
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


@api_view(['POST'])
def authorization_api_view(request):
    serializer = UserAuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data['username']
    password = serializer.validated_data['password']

    user = authenticate(
        username=username,
        password=password
    )

    if user:
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            'key': token.key
        })

    return Response(
        {'error': 'Unauthorized'},
        status=status.HTTP_401_UNAUTHORIZED
    )