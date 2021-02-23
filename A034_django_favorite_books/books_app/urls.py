from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>', views.show_book, name="show_book"),
    path('favorite/<int:pk>', views.add_favorite, name="favorite")
]