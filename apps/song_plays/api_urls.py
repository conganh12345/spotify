from django.contrib import admin
from django.urls import path
from . import api_views

urlpatterns = [
    path('songs/plays/<int:song_id>', api_views.count_plays, name='count_plays_song'),
    path('songs/plays', api_views.add_song_playszzzzzz, name='add_song_plays'),

]
