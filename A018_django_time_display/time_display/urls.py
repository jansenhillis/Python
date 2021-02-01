from django.urls import path
from . import views

urlpatterns = [
    path('', views.time_display),
    path('time_display', views.time_display),
]