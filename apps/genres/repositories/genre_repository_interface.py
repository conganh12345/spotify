from apps.cores.repositories.base_repository_interface import BaseRepositoryInterface
from abc import abstractmethod

class GenreRepositoryInterface(BaseRepositoryInterface):
   pass

   @abstractmethod
   def count_all_genre(self):
      pass