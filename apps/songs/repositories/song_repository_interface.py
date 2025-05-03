from apps.cores.repositories.base_repository_interface import BaseRepositoryInterface
from abc import abstractmethod

class SongRepositoryInterface(BaseRepositoryInterface):
   pass

   @abstractmethod
   def count_all_song(self):
      pass
