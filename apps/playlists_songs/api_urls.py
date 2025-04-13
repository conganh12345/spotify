from django.contrib import admin
from django.urls import path
from . import api_views

urlpatterns = [
    path('playlists/<int:playlist_id>', api_views.get_songs_in_playlist_id, name='get_songs_in_playlist_id'),
]
