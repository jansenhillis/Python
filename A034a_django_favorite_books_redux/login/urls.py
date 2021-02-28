from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout, name='logout'),
    path('success', views.success_view, name='success')
]
