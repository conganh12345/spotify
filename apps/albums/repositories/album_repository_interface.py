from apps.cores.repositories.base_repository_interface import BaseRepositoryInterface
from abc import abstractmethod

class AlbumRepositoryInterface(BaseRepositoryInterface):
   pass

   @abstractmethod
   def count_all_album(self):
      pass