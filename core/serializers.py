from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id' , 'username' , 'email' , 'password' , 'password_confirm']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        if validated_data['password'] == validated_data['password_confirm']:
            validated_data.pop('password_confirm')
            password =  validated_data.pop('password')
            User.objects.create(**validated_data , password = make_password(password))
            return validated_data
        raise serializers.ValidationError("password does not match")
    
    def update(self, instance, validated_data):
        # if validated_data['password'] == validated_data['password_confirm']:
        validated_data.pop('password_confirm')
        if 'password' in validated_data:
            instance.password = make_password(validated_data['password'])
        
        instance.save()
        return instance



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        # ...

        return token