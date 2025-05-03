from apps.cores.repositories.base_repository_interface import BaseRepositoryInterface
from abc import abstractmethod

class ArtistepositoryInterface(BaseRepositoryInterface):
    pass

    @abstractmethod
    def count_all_artist(self):
        pass