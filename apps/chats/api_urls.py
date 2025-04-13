from django.contrib import admin
from django.urls import path
from . import api_views

urlpatterns = [
    path('chats/', api_views.chat, name='chat'),
    

]
