from apps.cores.models import Song
from apps.cores.repositories.base_repository import BaseRepository
from apps.songs.repositories.song_repository_interface import SongRepositoryInterface

class SongRepository(BaseRepository, SongRepositoryInterface):
    def __init__(self):
        super().__init__(Song)
    def get_all_songs(self):
        return Song.objects.select_related('artist','genre','album').all()
    def get_song_id(self, id):
        return Song.objects.select_related('artist','genre','album').get(pk=id)
    

   
