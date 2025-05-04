from django.contrib import admin
from django.urls import path
from . import api_views

urlpatterns = [
    path('albums/plays/<int:album_id>', api_views.count_plays, name='count_plays'),
    path('albums/plays/', api_views.add, name='add'),
]
