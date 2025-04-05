from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='group_index'),
    path('create/', views.create_group, name='group_create'),
    path('edit/<int:group_id>/', views.edit_group, name='group_edit'),
    path('delete/<int:id>/', views.delete_group, name='group_delete'),
]
