from rest_framework.routers import DefaultRouter
from apps.genres.api_views import GenreViewSet

router = DefaultRouter()
router.register(r'genres', GenreViewSet, basename='genre')

urlpatterns = router.urls

#http://localhost:8000/api/genres/
