from rest_framework.routers import DefaultRouter
from apps.genres.api_views import GenreViewSet

router = DefaultRouter()
router.register(r'genres', GenreViewSet, basename='genre')

urlpatterns = router.urls
''' thêm thủ công
urlpatterns = router.urls + [
    path('genres/custom-action/', custom_view, name='genre-custom'),
]
'''
#http://localhost:8000/api/genres/
