from apps.cores.models import Song
from apps.cores.repositories.base_repository import BaseRepository
from apps.songs.repositories.song_repository_interface import SongRepositoryInterface
from django.db.models import Q

class SongRepository(BaseRepository, SongRepositoryInterface):
    def __init__(self):
        super().__init__(Song)
    def get_all_songs(self):
        return Song.objects.select_related('artist','genre','album').all()
    def get_song_id(self, id):
        return Song.objects.select_related('artist','genre','album').get(pk=id)
    def search_songs(self, keyword):
         return Song.objects.filter(
        Q(title__icontains=keyword) |
        Q(artist__name__iexact=keyword) | # iexact ko phân biệt hoa thường
        Q(album__title__iexact=keyword)
    )

    def get_songs_by_genre_id(self,genre_id):
        return Song.objects.filter(genre_id=genre_id)    
    '''Q(genre_name=keyword) |'''


   
