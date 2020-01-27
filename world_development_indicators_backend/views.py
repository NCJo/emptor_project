from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response

from .models import WorldDevelopmentIndicators
from .serializers import WdiSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView


class ListWorldDevelopmentIndicatorsView(ListCreateAPIView):
    queryset = WorldDevelopmentIndicators.objects.all()
    serializer_class = WdiSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, *kwargs)
    
class SingleDataView(RetrieveUpdateAPIView):
    queryset = WorldDevelopmentIndicators.objects.all()
    serializer_class = WdiSerializer

