from django.core.exceptions import ValidationError
from apps.songs.repositories.song_repository import SongRepository

class SongService:
    def __init__(self):
        self.song_repo = SongRepository()
    def get_song(self, song_id):
        return self.song_repo.get(song_id)
    
    def get_song_id(self,id):
        return self.song_repo.get_song_id(id)
    
    
    def get_all_songs(self):
        return self.song_repo.get_all_songs()

    def create_song(self, song_data):
         song = self.song_repo.create(**song_data)
         return song

    def update_song(self, song,  song_data):
        song_updated=self.song_repo.update(song, ** song_data)
        return song_updated

    def delete_song(self, song_id):
        song = self.song_repo.get(song_id)
        if not song:
            raise ValidationError('Bài hát không tồn tại')
        self.song_repo.delete(song)
        return True
    def search_song(self, keyword):
        return self.song_repo.search_songs(keyword)
    def get_songs_by_genre_id(self,genre_id):
        return self.song_repo.get_songs_by_genre_id(genre_id)