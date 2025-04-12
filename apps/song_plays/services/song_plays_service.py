from django.core.exceptions import ValidationError
from apps.song_plays.repositories.song_plays_repository import SongPlayRepository

class SongPlayService:
    def __init__(self):
        self.song_play_repo = SongPlayRepository()
    def add(self,user_id,song_id):
        return self.song_play_repo.add(user_id,song_id)
    def count_plays(self,song_id):
        return self.song_play_repo.count_plays(song_id)

    
