from apps.cores.models import Playlist
from apps.cores.repositories.base_repository import BaseRepository
from apps.playlists.repositories.playlists_repository_interface import PlaylistRepositoryInterface
from django.db.models import Q

class PlaylistRepository(BaseRepository, PlaylistRepositoryInterface):
    def __init__(self):
        super().__init__(Playlist)
    def get_playlists_user_id(self,user_id):
        return Playlist.objects.filter(user_id=user_id)
    def add(self, name, user_id):
        playlist = Playlist(name=name, user_id=user_id)
        playlist.save()
        return playlist
    def delete(self,playlist_id):
        Playlist.objects.get(id=playlist_id).delete()
    


   
