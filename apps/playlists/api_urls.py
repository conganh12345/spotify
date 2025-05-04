from django.contrib import admin
from django.urls import path
from . import api_views

urlpatterns = [
    path('playlists/', api_views.get_playlists_user_id, name='get_playlists_user_id'),
    path('playlists/<int:playlist_id>/', api_views.get_playlist_by_id_or_delete, name='get_playlist_by_id_or_delete'),
]
