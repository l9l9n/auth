from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

from .models import User
from rest_framework import serializers


class UserSerializers(ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "avatar", "background_img", "password", "confirm_password")

    # def validate_password(self, value):
    #     request = self.context.get("request")
    #     validate_password(value, request.user)
    #     return value

    # def validate(self, attrs):
    #     if attrs.get('password') != attrs.get('confirm_password'):
    #         raise serializers.ValidationError("Wrong password")
    #     return attrs
    #
    # def create(self, validated_data):
    #     data = User.objects.create(
    #         email=validated_data.get('email'),
    #         first_name=validated_data.get('first_name'),
    #         last_name=validated_data.get('last_name'),
    #         avatar=validated_data.get('avatar'),
    #         background_img=validated_data.get('background_img'),
    #         password=make_password(validated_data.get('password'))
    #     )
    #     return data


class UserListSerializer(ModelSerializer):

    class Meta:
        model = User
        exclude = ['password']
