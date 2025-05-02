from django.contrib import admin
from django.urls import path
from . import api_views

urlpatterns = [
    path('chats/<int:chat_id>/messages/', api_views.create_message, name='create_message'),
    path('chats/<int:chat_id>/', api_views.get_all_messages_chat_id, name='get_all_messages_chat_id'),
    

]
