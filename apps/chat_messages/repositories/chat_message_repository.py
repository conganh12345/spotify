from apps.cores.models import ChatMessage
from apps.cores.repositories.base_repository import BaseRepository
from apps.chat_messages.repositories.chat_message_repository_interface import ChatMessageRepositoryInterface
from django.utils import timezone
from django.db.models import Sum
from django.db.models import Q

class ChatMessageRepository(BaseRepository, ChatMessageRepositoryInterface):
      def __init__(self):
         super().__init__(ChatMessage)
      def get_chats_with_last_message(self,chats):
         last_messages = []
         for chat in chats:
            ''' select_relate chat cứ ko phải chat_id vì nhận tên field chứ ko phải tên cột '''
            last_message = ChatMessage.objects.filter(chat_id = chat.id).select_related('chat').order_by('-created_at').first()
            last_messages.append(last_message)
         return last_messages
      def create_message(self, message_text, chat_id, sender_id):
            ChatMessage.objects.create(
            message_text=message_text,
            chat_id=chat_id,
            sender_id=sender_id,
            is_read = False
            )
      def get_all_messages_chat_id(self,chat_id):
            return ChatMessage.objects.filter(chat_id=chat_id)


      
      
         
             
