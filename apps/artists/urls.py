from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='artist_index'),
    path('create/', views.create_artist, name='artist_create'),
    path('edit/<int:artist_id>/', views.edit_artist, name='artist_edit'),
    path('delete/<int:id>/', views.delete_artist, name='artist_delete'),
]
