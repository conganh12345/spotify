from django.contrib import admin
from django.urls import path
from . import api_views

urlpatterns = [
        path('albums/<album_id>/', api_views.get_albums, name='get_all_albums'),
]
