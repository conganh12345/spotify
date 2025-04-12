from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('artists/follow/<int:artist_id>', views.artist_follow, name='artist_follow'),
    path('artists/unfollow/<int:artist_id>', views.artist_unfollow, name='artist_unfollow'),
    path('artists/is_followed/<int:artist_id>', views.artist_is_followed, name='artist_is_followed'),
    path('artists/followed/', views.get_all_artist_follows, name='get_all_artist_follows'),

]
