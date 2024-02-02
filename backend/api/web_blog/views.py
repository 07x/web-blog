from django.shortcuts import render

# EXTERNAL IMPORTS 
from rest_framework.views import APIView 
from rest_framework import status 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated


# INTERNAL IMPORTS 
from .models import BlogPost
from django.contrib.auth import get_user_model
from .seriallizers import BlogPostSerializer

User = get_user_model()

class BlogPostView(APIView):
    permission_classes = [IsAuthenticated]    
    def get(self,request,format=None):
        user = request.user 
        objects = BlogPost.objects.filter(user=user)
        serializer = BlogPostSerializer(objects,many=True)
        response = {
            "message"       : "get blog post succesfully",
            "response_code" : 200,
            "data"          : serializer.data}
        return Response(response,status=status.HTTP_200_OK)


    def post(self,request,format=None):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message"       : "blog post saved succesfully",
                "response_code" : 201,
                "data"          : serializer.data}
            
            return Response(response,status=status.HTTP_201_CREATED)
        else:
            response = {
                "message"       : serializer.errors,
                "response_code" : 400,
                "data"          : []
            }
            return Response(response,status=status.HTTP_400_BAD_REQUEST)




