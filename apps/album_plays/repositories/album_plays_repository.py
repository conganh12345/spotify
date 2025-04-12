from apps.cores.models import AlbumPlay
from apps.cores.repositories.base_repository import BaseRepository
from apps.album_plays.repositories.album_plays_repository_interface import AlbumPlayRepositoryInterface
from django.utils import timezone
from django.db.models import Sum

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
