from apps.cores.models import PlaylistSong
from apps.cores.repositories.base_repository import BaseRepository
from apps.playlists_songs.repositories.playlists_songs_repository_interface import PlaylistSongRepositoryInterface
from django.db.models import Q

class PlaylistSongRepository(BaseRepository, PlaylistSongRepositoryInterface):
    def __init__(self):
        super().__init__(PlaylistSong)
    def get_songs_in_playlist_id(self,playlist_id):
        return PlaylistSong.objects.filter(playlist_id==playlist_id).select_related('song').all()
    def is_added_before(self,song_id, playlist_id):
        try:
            return PlaylistSong.objects.get(song_id=song_id,playlist_id=playlist_id)
        except PlaylistSong.DoesNotExist:
            return None
    def add(self,song_id,playlist_id):
        PlaylistSong.objects.create(playlist_id=playlist_id,song_id=song_id)
    def delete(self,song_id,playlist_id):
        playlist_song = PlaylistSong.objects.get(song_id=song_id,playlist_id=playlist_id)
        '''
        PlaylistSong.objects.filter(song_id=song_id, playlist_id=playlist_id).delete()
        '''
        playlist_song.delete()
        
    def delete_all_songs_playlist_id(self,playlist_id):
        PlaylistSong.objects.filter(playlist_id=playlist_id).delete()
            
        
    


   
