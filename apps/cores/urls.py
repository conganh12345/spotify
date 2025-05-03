from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dashboard_index'),
    path('api/songs/plays/', views.get_song_plays, name='get_song_plays'),
    path('api/albums/plays/', views.get_album_plays, name='get_album_plays'),
]
