from rest_framework.routers import DefaultRouter
from apps.genres.api_views import GenreViewSet
from . import api_views
from django.urls import path

router = DefaultRouter()
router.register(r'genres', GenreViewSet, basename='genre')

urlpatterns = router.urls
urlpatterns = router.urls + [
    path('genres/genres/<int:genre_id>', api_views.get_songs_by_genre_id, name='genre-custom'),
]

#http://localhost:8000/api/genres/
