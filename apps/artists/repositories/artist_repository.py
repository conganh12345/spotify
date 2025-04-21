from apps.artists.models import Artist
from apps.cores.repositories.base_repository import BaseRepository
from apps.artists.repositories.artist_repository_interface import ArtistepositoryInterface

class ArtistRepository(BaseRepository, ArtistepositoryInterface):
    def __init__(self):
        super().__init__(Artist)
    
    def search_artist(self, keyword):
        return Artist.objects.filter(name__icontains=keyword)
    
    def get_artist_id(self, id):
        return Artist.objects.prefetch_related('songs__album').get(pk=id)



