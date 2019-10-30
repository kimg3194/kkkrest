from .models import Post
from .serializer import PostSerializer

from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets

from rest_framework import renderers
from rest_framework.decorators import action 
from django.http import HttpResponse

class MyPagination(PageNumberPagination):
  page_size = 5

class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all().order_by('id')
  serializer_class = PostSerializer
  pagination_class = MyPagination