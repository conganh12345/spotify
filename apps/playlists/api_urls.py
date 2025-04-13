from django.contrib import admin
from django.urls import path
from . import api_views

urlpatterns = [
    path('playlists/', api_views.get_playlists_user_id, name='get_playlists_user_id'),
]
