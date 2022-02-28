from django.shortcuts import render

from rest_framework.generics import ListAPIView
from .serializers import BookSerializer
from .models import Book


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    class_serializer = BookSerializer
