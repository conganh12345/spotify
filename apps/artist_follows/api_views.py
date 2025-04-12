from rest_framework import viewsets
from apps.cores.models import ArtistFollow
from apps.artist_follows.serializers import ArtistFollowsSerializer

class ArtistFollowViewSet(viewsets.ModelViewSet):
    queryset = ArtistFollow.objects.all()
    serializer_class = ArtistFollowsSerializer
