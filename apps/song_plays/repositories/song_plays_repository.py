from apps.cores.models import SongPlay
from apps.cores.repositories.base_repository import BaseRepository
from apps.song_plays.repositories.song_plays_repository_interface import SongPlayRepositoryInterface
from django.utils import timezone
from django.db.models import Sum

class SongPlayRepository(BaseRepository, SongPlayRepositoryInterface):
      def __init__(self):
         super().__init__(SongPlay)
      def is_played_before(self, user_id, song_id):
          try:
              return SongPlay.objects.get(user_id=user_id,song_id=song_id)
          except SongPlay.DoesNotExist:
              return None
      
      def add(self, user_id, song_id):
           song_play = self.is_played_before(user_id,song_id)
           if song_play:
               song_play.played_at = timezone.now()
               song_play.plays_count +=1
               song_play.save()
           else:
               SongPlay.objects.create(play_counts = 1 , song_id=song_id, user_id = user_id)
      def count_plays(self,song_id):
            result =  SongPlay.objects.filter(song_id=song_id).aggregate(total=Sum('plays_count'))
            return result['total'] or 0   
                