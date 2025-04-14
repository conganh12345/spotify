from django.core.exceptions import ValidationError
from apps.chats.repositories.chat_repository import ChatRepository

class ChatService:
    def __init__(self):
        self.chat_repo = ChatRepository()
        
    def is_created_before(self,user1_id,user2_id):
        return self.chat_repo.is_created_before(user1_id=user1_id,user2_id=user2_id)
    def add(self,user1_id,user2_id):
        self.chat_repo.add(user1_id=user1_id,user2_id=user2_id)
    def get_all_chats_by_userid(self, user_id):
        return self.chat_repo.get_all_chats_by_userid(user_id)

    
