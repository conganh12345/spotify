from apps.cores.models import Chat
from apps.cores.repositories.base_repository import BaseRepository
from apps.chats.repositories.chat_repository_interface import ChatRepositoryInterface
from django.utils import timezone
from django.db.models import Sum
from django.db.models import Q

class ChatRepository(BaseRepository, ChatRepositoryInterface):
      def __init__(self):
         super().__init__(Chat)
      def is_created_before(self, user1_id, user2_id):
         a_exists = Chat.objects.filter(user1_id=user1_id, user2_id=user2_id).exists()
         b_exists = Chat.objects.filter(user1_id=user2_id, user2_id=user1_id).exists()
         return a_exists or b_exists


   
      def add(self,user1_id,user2_id):
          Chat.objects.create(user1_id=user1_id,user2_id=user2_id)
         
      def get_all_chats_by_userid(self, user_id):
         return Chat.objects.filter(Q(user1_id=user_id) | Q(user2_id=user_id))
      
      def get_all_chats(self):
         return Chat.objects.select_related('user1', 'user2').all()
      def get_chat_by_id(self, id):
         return Chat.objects.select_related('user1', 'user2').get(id=id)

      
         
             
