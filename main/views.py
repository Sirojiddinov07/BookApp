from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .models import *
from .serializers import *


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ProductView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAdminUser]


class CreateProductView(generics.CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAdminUser]



