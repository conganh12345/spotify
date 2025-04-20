from rest_framework.routers import DefaultRouter
from apps.genres.api_views import GenreViewSet
from . import api_views
from django.urls import path

router = DefaultRouter()
router.register(r'genres', GenreViewSet, basename='genre')

urlpatterns = router.urls
urlpatterns = router.urls + [
    path('playlists/', api_views.get_playlists_user_id, name='get_playlists_user_id'),
]

#http://localhost:8000/api/genres/
