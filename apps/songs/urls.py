from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='song_index'),
    path('create/', views.create_song, name='song_create'),
    path('edit/<int:song_id>/', views.edit_song, name='song_edit'),
    path('delete/<int:id>/', views.delete_song, name='song_delete'),
    path('song_file/<int:id>/', views.song_file, name='song_file'),
    path('song_video/<int:id>/', views.song_video, name='song_video'),

]
