from django.contrib import admin
from django.urls import path
from . import api_views

urlpatterns = [
    path('songs/', api_views.search_songs, name='search_songs'),
]
