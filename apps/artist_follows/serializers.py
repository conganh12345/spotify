from rest_framework import serializers
from apps.cores.models import ArtistFollow

class ArtistFollowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistFollow
        fields = ['user', 'artist', 'followed_at']
