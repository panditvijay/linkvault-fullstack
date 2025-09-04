from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer