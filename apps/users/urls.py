from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('', views.index, name='user_index'),
    path('create/', views.create_user, name='user_create'),
    path('edit/<int:user_id>/', views.edit_user, name='user_edit'),
    path('delete/<int:id>/', views.delete_user, name='user_delete'),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
