import secrets

from django.conf import settings
from django.urls import reverse
from rest_framework import status, generics
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .utils import send_email
from .serializers import UserSerializers, UserListSerializer

import jwt


class RegisterViewSet(generics.CreateAPIView):
    serializer_class = UserSerializers
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        print(self)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token = secrets.token_hex(16)
        print(token)

        relativelink = reverse('email-verify')

        absurl = f'http://localhost:8000' + relativelink + "?token=" + str(token)

        email_body = 'hi' + user.username + 'use link below to verify your email \n' + absurl
        data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Verify your email'}

        send_email(data)

        return Response({'status': 'success'})


class LoginViewSet(TokenObtainPairView):
    permission_classes = [AllowAny]


class VerifyEmail(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, request):
        token = request.GET.get('token')
        try:
            # payload = jwt.decode(token, settings.SECRET_KEY)
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid Token'}, status=status.HTTP_400_BAD_REQUEST)

        payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
