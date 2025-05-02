from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='chat_index'),
    path('detail/<int:id>', views.detail_chat, name='detail_chat'),
    path('delete/<int:id>', views.delete_chat, name='delete_chat'),
]
