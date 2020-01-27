from django.urls import path
from . import views

from .views import ListWorldDevelopmentIndicatorsView

urlpatterns = [
    path('', ListWorldDevelopmentIndicatorsView.as_view(), name="wdi-all")
]
