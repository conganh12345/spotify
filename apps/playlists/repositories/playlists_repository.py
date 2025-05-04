from apps.cores.models import Playlist
from apps.cores.models import PlaylistSong
from apps.cores.repositories.base_repository import BaseRepository
from apps.playlists.repositories.playlists_repository_interface import PlaylistRepositoryInterface
from django.db.models import Q
from django.db.models import Prefetch

class PlaylistRepository(BaseRepository, PlaylistRepositoryInterface):
    def __init__(self):
        super().__init__(Playlist)
    def get_by_id(self, playlist_id):
        return Playlist.objects.filter(id=playlist_id).first()
    def get_playlists_user_id(self,user_id):
        return Playlist.objects.filter(user_id=user_id)\
        .prefetch_related(
            Prefetch(
                'playlistsong_set',  
                queryset=PlaylistSong.objects.select_related('song')  
            )
        )

    def add(self, name, user_id):
        playlist = Playlist(name=name, user_id=user_id)
        playlist.save()
        return playlist
    def delete(self,playlist_id):
        Playlist.objects.get(id=playlist_id).delete()
    
    def get_all_playlists(self):
        return Playlist.objects.select_related('user').all()
    
    def get_playlist_with_songs_details(self, playlist_id):
        playlist = Playlist.objects.prefetch_related(
            'songs__artist', 'songs__album', 'songs__genre'
        ).get(id=playlist_id)
        return playlist


   
