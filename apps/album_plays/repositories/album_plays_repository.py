from apps.cores.models import AlbumPlay
from apps.cores.repositories.base_repository import BaseRepository
from apps.album_plays.repositories.album_plays_repository_interface import AlbumPlayRepositoryInterface
from django.utils import timezone
from django.db.models import Sum
from datetime import datetime, timedelta

class AlbumPlayRepository(BaseRepository, AlbumPlayRepositoryInterface):
      def __init__(self):
         super().__init__(AlbumPlay)
      def is_played_before(self, user_id, album_id):
            try:
               return AlbumPlay.objects.get(user_id=user_id,album_id=album_id)
            except AlbumPlay.DoesNotExist:
               return None
      def add(self, user_id, album_id):
         album_play = self.is_played_before(user_id,album_id)
         if album_play:
            album_play.plays_count+=1
            album_play.played_at = timezone.now()  
            album_play.save()
         else:
            AlbumPlay.objects.create(
               user_id=user_id,
               plays_count = 1,
               album_id=album_id
               )
      def count_plays(self, album_id):
         result = AlbumPlay.objects.filter(album_id=album_id).aggregate(total=Sum('plays_count'))
         return result['total'] or 0        

      def get_album_play_stats_last_15_days(self):
        end_date = timezone.now().date()
        start_date = end_date - timedelta(days=14)
        stats = {}

        for single_date in (start_date + timedelta(n) for n in range(15)):
            date_str = single_date.strftime('%Y-%m-%d')

            day_start = timezone.make_aware(datetime.combine(single_date, datetime.min.time()))
            day_end = day_start + timedelta(days=1)

            total_plays = AlbumPlay.objects.filter(
                played_at__gte=day_start,
                played_at__lt=day_end
            ).aggregate(total=Sum('plays_count'))['total'] or 0
            stats[date_str] = total_plays

        return stats