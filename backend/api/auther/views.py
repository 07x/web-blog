from django.shortcuts import render
# JWT 
from rest_framework_simplejwt.tokens import RefreshToken

# EXTERNAL IMPORTS
from rest_framework.views import APIView 
from rest_framework import status 
from rest_framework.response import Response 

# INTERNAL IMPORTS
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from .serializers import UserSerializer , RegistrationSerializer
User = get_user_model()

# Registration 
class RegistrationView(APIView):
    def post(self,request,foramt=None):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message"       : "you are register successfuly",
                "response_code" : 201, 
                "data"          : serializer.data 
            }
            return Response(response,status=status.HTTP_201_CREATED)

# LOGIN VIEWS 
class LoginView(APIView):
    def post(self,request,foramt=None):
        data = request.data
        # AUTHNICATION
        user = authenticate(request,email=data.get('email'),password=data.get('password'))
        if user:
            refresh = RefreshToken.for_user(user)
            serializer = UserSerializer(user)
            response = {
                    "messege"       : "login successfully",
                    "response_code" : 200, 
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "data"          : serializer.data 

                }
            return Response(response,status=status.HTTP_200_OK)
        else:
            response = {
                "messege"       : 'unable to find user with this credintials',
                "response_code" : 400, 
                "data"          : []
            }
            return Response(response,status=status.HTTP_400_BAD_REQUEST)



