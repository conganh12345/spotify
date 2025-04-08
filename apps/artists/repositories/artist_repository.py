from apps.artists.models import Artist
from apps.cores.repositories.base_repository import BaseRepository
from apps.artists.repositories.artist_repository_interface import ArtistepositoryInterface

class ArtistRepository(BaseRepository, ArtistepositoryInterface):
    def __init__(self):
        super().__init__(Artist)


