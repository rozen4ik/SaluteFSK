from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('identifier/', views.info_card),
    path('passage/', views.passage_card),
]
