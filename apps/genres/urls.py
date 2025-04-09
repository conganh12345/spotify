from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='genre_index'),
    path('create/', views.create_genre, name='genre_create'),
    path('edit/<int:genre_id>/', views.edit_genre, name='genre_edit'),
    path('delete/<int:id>/', views.delete_genre, name='genre_delete'),
]
