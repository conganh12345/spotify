from apps.cores.models import SongPlay
from apps.cores.repositories.base_repository import BaseRepository
from apps.song_plays.repositories.song_plays_repository_interface import SongPlayRepositoryInterface
from django.utils import timezone
from django.db.models import Sum
from datetime import datetime, timedelta

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
      
      def is_played_before(self, user_id, song_id):
        try:
            return SongPlay.objects.get(user_id=user_id, song_id=song_id)
        except SongPlay.DoesNotExist:
            return None
        
      def get_play_stats_last_15_days(self):
        end_date = timezone.now().date()
        start_date = end_date - timedelta(days=14)
        stats = {}

        for single_date in (start_date + timedelta(n) for n in range(15)):
            date_str = single_date.strftime('%Y-%m-%d')
            # Define the start and end of the day
            day_start = timezone.make_aware(datetime.combine(single_date, datetime.min.time()))
            day_end = day_start + timedelta(days=1)
            # Filter records within the day's range
            total_plays = SongPlay.objects.filter(
                played_at__gte=day_start,
                played_at__lt=day_end
            ).aggregate(total=Sum('plays_count'))['total'] or 0
            stats[date_str] = total_plays

        return stats
        
                