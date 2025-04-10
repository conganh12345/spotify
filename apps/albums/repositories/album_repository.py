from apps.cores.models import Album
from apps.cores.repositories.base_repository import BaseRepository
from apps.albums.repositories.album_repository_interface import AlbumRepositoryInterface

class AlbumRepository(BaseRepository, AlbumRepositoryInterface):
    def __init__(self):
        super().__init__(Album)
    def get_all_albums(self):
        return Album.objects.select_related('artist').all()
    def get_album_id(self, id):
        return Album.objects.select_related('artist').get(pk=id)



   
