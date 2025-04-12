from django.contrib import admin
from django.urls import path
from . import api_views

urlpatterns = [
    path('album/plays/<int:album_id>', api_views.count_plays, name='count_plays'),
    path('album/plays/', api_views.add, name='add'),

]
