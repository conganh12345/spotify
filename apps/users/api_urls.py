from django.contrib import admin
from django.urls import path
from . import api_views
from rest_framework_simplejwt.views import TokenRefreshView
from .api_views import UserUpdateView
from .api_views import SignupView

urlpatterns = [
    path('api/token/', api_views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('signup/', SignupView.as_view(), name='signup')
]
