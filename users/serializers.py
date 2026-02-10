from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import random
from .models import Confirm

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, data):
        user = User(username=data["username"], is_active=False)
        user.set_password(data["password"])
        user.save()
        code = str(random.randint(100000, 999999))
        Confirm.objects.create(user=user,code=code )
        return {"user": user, "code": code}

class ConfirmSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField()
    def validate(self, data):
        user = User.objects.get(username=data["username"])
        confirm = Confirm.objects.get(user=user)
        if confirm.code != data["code"]:
            raise serializers.ValidationError("Wrong code")
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    def validate(self, data):
        user = authenticate(
            username=data["username"],
            password=data["password"]
        )
        if not user:
            raise serializers.ValidationError("Wrong username or password")
        if not user.is_active:
            raise serializers.ValidationError("User not confirmed")
        return user
