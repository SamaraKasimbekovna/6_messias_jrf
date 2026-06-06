# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.authtoken.models import Token
#
# from .serializers import RegisterSerializer, LoginSerializer
#
#
# class RegisterView(APIView):
#
#     def post(self, request):
#
#         serializer = RegisterSerializer(data=request.data)
#
#         serializer.is_valid(raise_exception=True)
#
#         user = serializer.save()
#
#         token, created = Token.objects.get_or_create(user=user)
#
#         return Response(
#             {
#                 "token": token.key,
#                 "email": user.email
#             },
#             status=status.HTTP_201_CREATED
#         )
#
#
# class LoginView(APIView):
#
#     def post(self, request):
#
#         serializer = LoginSerializer(data=request.data)
#
#         serializer.is_valid(raise_exception=True)
#
#         user = serializer.validated_data["user"]
#
#         token, created = Token.objects.get_or_create(user=user)
#
#         return Response(
#             {
#                 "token": token.key
#             },
#             status=status.HTTP_200_OK
#         )

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (
    RegisterSerializer,
    MyTokenObtainPairSerializer
)


class RegisterView(APIView):

    def post(self, request):

        serializer = RegisterSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        user = serializer.save()

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            },
            status=status.HTTP_201_CREATED
        )


class LoginView(TokenObtainPairView):
    serializer_class = (
        MyTokenObtainPairSerializer
    )