from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('random_word', views.random_word),
    path('random_word/reset', views.reset),
]