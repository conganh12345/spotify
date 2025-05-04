from apps.cores.repositories.base_repository_interface import BaseRepositoryInterface
from abc import abstractmethod

class PlaylistRepositoryInterface(BaseRepositoryInterface):
   pass

@abstractmethod
def get_all_playlists(self):
   pass