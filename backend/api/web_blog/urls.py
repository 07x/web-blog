
from django.urls import path
from .views import BlogPostView 

urlpatterns = [

path('blog/',BlogPostView.as_view(),name='blog')

]
