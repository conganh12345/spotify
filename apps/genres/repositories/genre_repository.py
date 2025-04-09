from apps.cores.models import Genre
from apps.cores.repositories.base_repository import BaseRepository
from apps.genres.repositories.genre_repository_interface import GenreRepositoryInterface

class GenreRepository(BaseRepository, GenreRepositoryInterface):
    def __init__(self):
        super().__init__(Genre)

   
