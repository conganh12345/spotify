from apps.cores.models import Album
from apps.cores.repositories.base_repository import BaseRepository
from apps.albums.repositories.album_repository_interface import AlbumRepositoryInterface
from apps.cores.models import Song
from django.db.models import Q

class AlbumRepository(BaseRepository, AlbumRepositoryInterface):
    def __init__(self):
        super().__init__(Album)
    def get_all_albums(self):
        return Album.objects.select_related('artist').all()
    def get_album_id(self, id):
        return Album.objects.select_related('artist').get(pk=id)
    def get_all_songs_album_id(self,id):
        return Song.objects.filter(album_id=id).select_related('artist','genre','album')
    def search_album(self,keyword):
        return Album.objects.filter(
            Q(title_icontains=keyword)|
            Q(artist_name_icontains = keyword)
        )

   
