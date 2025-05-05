from django.contrib import admin
from django.urls import path
from . import api_views

urlpatterns = [
    path('chats/', api_views.chat, name='chat'),
    path('chats/is_created', api_views.chat_create, name='chat'),


]
