from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.new),
    path('shows/create', views.create),
    path('shows/<int:show_id>', views.show_description, name="show_details"),
    path('shows/<int:show_id>/edit', views.edit, name="edit_view"),
    path('shows/<int:show_id>/update', views.update, name="update"),
    path('shows/<int:show_id>/destroy', views.destroy, name="destroy"),
]   
