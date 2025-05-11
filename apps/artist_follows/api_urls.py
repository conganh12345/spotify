from django.contrib import admin
from django.urls import path
from . import api_views

urlpatterns = [
    path('artists/follow/', api_views.artist_follow, name='artist_follow'),
    path('artists/unfollow/<int:artist_id>', api_views.artist_unfollow, name='artist_unfollow'),
    path('artists/is_followed/<int:artist_id>', api_views.artist_is_followed, name='artist_is_followed'),
    path('artists/followed/', api_views.get_all_artist_follows, name='get_all_artist_follows'),
    path('artists/count_artist/<int:artist_id>', api_views.count, name='count'),
]
