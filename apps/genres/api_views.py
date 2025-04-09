from rest_framework import viewsets
from apps.cores.models import Genre
from apps.genres.serializers import GenreSerializer

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
