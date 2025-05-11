from apps.cores.models import ArtistFollow
from apps.cores.repositories.base_repository import BaseRepository
from apps.artist_follows.repositories.artist_follows_repository_interface import ArtistFollowRepositoryInterface

class ArtistFollowRepository(BaseRepository, ArtistFollowRepositoryInterface):
    def __init__(self):
        super().__init__(ArtistFollow)
    def get_by_user_and_artist(self, user_id, artist_id):
        try:
            return ArtistFollow.objects.get(user_id=user_id, artist_id=artist_id)
        except ArtistFollow.DoesNotExist:
            return None

    def add(self, user_id, artist_id):
        return ArtistFollow.objects.create(user_id=user_id, artist_id=artist_id)

    def delete_by_user_and_artist(self, user_id, artist_id):
        follow = self.get_by_user_and_artist(user_id, artist_id)
        if follow:
            follow.delete()
            return True
        return False
    
    def get_all_artist_follows(self,user_id):
        return ArtistFollow.objects.filter(user_id=user_id).select_related('artist')
    def count(self,artist_id):
        return ArtistFollow.objects.filter(artist_id=artist_id).count()
