from django.core.exceptions import ValidationError
from apps.playlists_songs.repositories.playlists_songs_repository import PlaylistSongRepository

class PlaylistSongService:
    def __init__(self):
        self.playlists_songs_repo = PlaylistSongRepository()

    def get_songs_in_playlist_id(self, playlist_id):
        return self.playlists_songs_repo.get_songs_in_playlist_id(playlist_id)
    def is_added_before(self,playlist_id,song_id):
        return self.playlists_songs_repo.is_added_before(playlist_id=playlist_id,song_id=song_id)
    def add(self,playlist_id,song_id):
        self.playlists_songs_repo.add(playlist_id=playlist_id,song_id=song_id)
    def delete(self,playlist_id,song_id):
        self.playlists_songs_repo.delete(playlist_id=playlist_id,song_id=song_id)
    def delete_all_songs_playlist_id(self,playlist_id):
        self.playlists_songs_repo.delete_all_songs_playlist_id(playlist_id)
    
