from django.urls import path, re_path
from . import views

from .views import ListWorldDevelopmentIndicatorsView, SingleDataView
# , DetailView

urlpatterns = [
    # path('', views.index, name='index'),
    path('', ListWorldDevelopmentIndicatorsView.as_view(), name="wdi-all"),
    path('<int:pk>', SingleDataView.as_view()),

]
