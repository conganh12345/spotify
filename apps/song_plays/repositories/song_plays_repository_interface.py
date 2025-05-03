from apps.cores.repositories.base_repository_interface import BaseRepositoryInterface
from abc import abstractmethod

class SongPlayRepositoryInterface(BaseRepositoryInterface):
   pass

   @abstractmethod
   def add(self, user_id, song_id):
      pass

   @abstractmethod
   def count_plays(self, song_id):
      pass

   @abstractmethod
   def get_song_play_stats_last_15_days(self):
      pass
