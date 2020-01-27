from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import WorldDevelopmentIndicators
from .serializers import WdiSerializer


# Create your views here.
# def index(request):
#     return HttpResponse('<h1>Hello</h1>')

class ListWorldDevelopmentIndicatorsView(generics.ListAPIView):
    '''
    Provide GET method handler
    '''

    queryset = WorldDevelopmentIndicators.objects.all()
    serializer_class = WdiSerializer