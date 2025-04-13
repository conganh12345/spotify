from django.core.exceptions import ValidationError
from apps.album_plays.repositories.album_plays_repository import AlbumPlayRepository

class AlbumPlayService:
    def __init__(self):
        self.album_play_repo = AlbumPlayRepository()
    def add(self,user_id,album_id):
        return self.album_play_repo.add(user_id,album_id)
    def count_plays(self,album_id):
        return self.album_play_repo.count_plays(album_id)

    
