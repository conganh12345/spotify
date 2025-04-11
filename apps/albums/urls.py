from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='album_index'),
    path('create/', views.create_album, name='album_create'),
    path('edit/<int:album_id>/', views.edit_album, name='album_edit'),
    path('delete/<int:id>/', views.delete_album, name='album_delete'),
    path('detail/<int:id>/', views.detail_album, name='detail_album'),
    path('detail/delete/<int:id>/', views.delete_song_in_album, name='delete_song_in_album'),
    path('detail/add/<int:song_id>/<int:album_id>', views.add_song_in_album, name='add_song_in_album'),

]
