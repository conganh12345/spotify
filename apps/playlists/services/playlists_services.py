from django.core.exceptions import ValidationError
from apps.playlists.repositories.playlists_repository import PlaylistRepository

class PlaylistService:
    def __init__(self):
        self.playlist_repo = PlaylistRepository()
    def get_playlists_user_id(self,user_id):
        return self.playlist_repo.get_playlists_user_id(user_id)
    def add(self,name,user_id):
        return self.playlist_repo.add(name=name,user_id=user_id)
    def delete(self,playlist_id):
        self.playlist_repo.delete(playlist_id)