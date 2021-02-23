from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>', views.show_book, name="show_book"),
    path('favorite/<int:pk>', views.add_favorite, name="favorite"),
    path('remove/<int:pk>', views.remove_favorite, name="remove"),
    path('process_book/', views.process_book, name="process"),
    path('update_book/<int:pk>', views.update_book, name="update"),
    path('delete_book/<int:pk>', views.delete_book, name="delete")
]