from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Author
from .serializers import AuthSerializer


class AuthorListView(ListAPIView):
    queryset = Author.objects.all()
    class_serializer = AuthSerializer

