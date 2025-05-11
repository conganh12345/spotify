from django.core.exceptions import ValidationError
from apps.playlists.repositories.playlists_repository import PlaylistRepository
from apps.cores.models import Playlist


class PlaylistService:
    def __init__(self):
        self.playlist_repo = PlaylistRepository()
    def get_by_id(self,user_id):
        return self.playlist_repo.get_by_id(user_id)
    def get_playlists_user_id(self,user_id):
        return self.playlist_repo.get_playlists_user_id(user_id)
    
    def add(self,name,user_id):
        return self.playlist_repo.add(name=name,user_id=user_id)
    
    def delete(self,playlist_id):
        self.playlist_repo.delete(playlist_id)
    
    def get_all_playlists(self):
        return self.playlist_repo.get_all_playlists()
    
    def get_playlist_details(self, playlist_id):
        return self.playlist_repo.get_playlist_with_songs_details(playlist_id)
    def update_name_playlist(self,playlist_id,name):
        return self.playlist_repo.update_name_playlist(playlist_id,name)