from rest_framework import serializers 
from django.contrib.auth import get_user_model

# EXTERNAL IMPORTS
from rest_framework.views import APIView 
from rest_framework import status 
from rest_framework.response import Response 

User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'mobile_number', 'type', 'avatar']
        extra_kwargs = {
            'email': {'validators': []},  # Remove the default unique validator
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        if User.objects.filter(email=validated_data["email"]).exists():
            response = {
                "message": "User Already Exists",
                "response_code": 400,
                "data": []
            }
            raise serializers.ValidationError(response)

        # Use the correct serializer class here (self instead of UserSerializer)
        user = super(RegistrationSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

# create serializer here 
class UserSerializer(serializers.ModelSerializer):
    """
        we cannot use both fields and exclude in the Meta Class of your serializer
    """

    class Meta:
        model  = User 
        fields = ['type','email','first_name','last_name','mobile_number','date_joined'] 


