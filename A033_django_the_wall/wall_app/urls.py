from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('post/', views.post_message, name='post'),
    path('comment/', views.comment, name='comment')
]

