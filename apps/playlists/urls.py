from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='playlist_index'),
    path('detail/<int:id>/', views.detail_playlist, name='detail_playlist'),
]
