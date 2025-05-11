from django.core.exceptions import ValidationError
from apps.artist_follows.repositories.artist_follows_repository import ArtistFollowRepository

class ArtistFollowService:
    def __init__(self):
        self.artist_follow_repo = ArtistFollowRepository()
    def get_by_user_and_artist(self,user_id, artist_id):
        return self.artist_follow_repo.get_by_user_and_artist(user_id,artist_id)
    def add(self,user_id, artist_id):
        return self.artist_follow_repo.add(user_id,artist_id)
    def delete_by_user_and_artist(self,user_id, artist_id):
        return self.artist_follow_repo.delete_by_user_and_artist(user_id,artist_id)
    def get_all_artist_follows(self,user_id):
        return self.artist_follow_repo.get_all_artist_follows(user_id)
    def count(self,artist_id):
        return self.artist_follow_repo.count(artist_id)
    
