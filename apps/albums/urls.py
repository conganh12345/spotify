from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='album_index'),
    path('create/', views.create_album, name='album_create'),
    path('edit/<int:album_id>/', views.edit_album, name='album_edit'),
    path('delete/<int:id>/', views.delete_album, name='album_delete'),
]
