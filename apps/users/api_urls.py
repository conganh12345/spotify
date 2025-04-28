from django.contrib import admin
from django.urls import path
from . import api_views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('api/token/', api_views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
