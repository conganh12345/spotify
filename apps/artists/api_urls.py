from django.contrib import admin
from django.urls import path
from . import api_views

urlpatterns = [
    path('artists/<artist_id>/', api_views.get_artists_id, name='get_all_artists'),
    path('artists/', api_views.get_all_artists, name='get_all_artists'),
]
