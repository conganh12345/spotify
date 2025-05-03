from apps.cores.repositories.base_repository_interface import BaseRepositoryInterface
from abc import abstractmethod

class AlbumPlayRepositoryInterface(BaseRepositoryInterface):
   pass

   @abstractmethod
   def get_album_play_stats_last_15_days(self):
      pass
