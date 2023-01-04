from rest_framework import serializers
from users.models import User

import ipdb

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["is_superuser"] = user.is_superuser

        return token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=["id","name","birthdate","cpf", "email", "password","is_superuser", "is_active"]
        extra_kwargs={"password":{"write_only":True}}

    def create(self, validated_data):
        email=validated_data["email"]
        username=""
        for word in email:
            if word == "@":
                break
            username= username + word
        
        validated_data["username"]= username
        try:
            employee = validated_data.pop("is_superuser")
            if employee:
             user = User.objects.create_superuser(**validated_data, is_superuser=True)
             return user 
        except KeyError:
             user= User.objects.create_user(**validated_data, is_superuser=False)
             return user
            
       
        

    def validate_cpf(self, cpf):
        cpf_already_exists= User.objects.filter(cpf=cpf).exists()
        if cpf_already_exists:
            raise serializers.ValidationError(detail="CPF já cadastrado")
        return cpf
    def validate_email(self, email):
        email_already_exists = User.objects.filter(email = email).exists()
        if email_already_exists:
            raise serializers.ValidationError(detail= "email already registered.")
        return email