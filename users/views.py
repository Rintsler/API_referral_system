from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.conf import settings
import random

from users.models import User
from users.serializer import UserSerializer


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SendConfirmationCode(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')

        # Проверка, существует ли пользователь с указанным номером телефона
        if User.objects.filter(phone_number=phone_number).exists():
            return Response({'error': 'User with this phone number already exists'}, status=status.HTTP_400_BAD_REQUEST)

        # Генерация кода подтверждения
        confirmation_code = ''.join(random.choices('0123456789', k=settings.CONFIRMATION_CODE_LENGTH))

        # Отправка кода подтверждения (здесь предполагается использование стороннего сервиса для отправки SMS или электронной почты)
        # Например:
        # send_confirmation_code_via_sms(phone_number, confirmation_code)

        return Response({'message': 'Confirmation code sent successfully'})


class VerifyConfirmationCode(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        confirmation_code = request.data.get('confirmation_code')

        # Проверка существования пользователя с указанным номером телефона
        user = User.objects.filter(phone_number=phone_number).first()
        if not user:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        # Проверка совпадения кода подтверждения
        if confirmation_code != user.invite_code_active:
            return Response({'error': 'Invalid confirmation code'}, status=status.HTTP_400_BAD_REQUEST)

        # Успешная проверка кода подтверждения
        # Можно выполнить здесь необходимые действия, например, создать пользователя или вернуть токен аутентификации

        return Response({'message': 'Confirmation code verified successfully'})
