from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Project
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "password"]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['user_id'] = user.id
        token['username'] = user.username
        token['first_name'] = user.first_name

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        data.update({'user_id': self.user.id})
        data.update({'username': self.user.username})
        data.update({'first_name': self.user.first_name})

        return data


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "title", "description",
                  "image", "created_at", "updated_at"]
        extra_kwargs = {'user': {'write_only': True}}
