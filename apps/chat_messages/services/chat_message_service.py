from django.core.exceptions import ValidationError
from apps.chat_messages.repositories.chat_message_repository import ChatMessageRepository

class ChatMessageService:
    def __init__(self):
        self.chat_message_repo = ChatMessageRepository()
    def get_chats_with_last_message(self,chats):
        return self.chat_message_repo.get_chats_with_last_message(chats)
    
    def create_message(self,message_text, chat_id, sender_id):
        self.chat_message_repo.create_message(chat_id=chat_id,message_text=message_text,sender_id=sender_id)
    def get_all_messages_chat_id(self,chat_id):
        return self.chat_message_repo.get_all_messages_chat_id(chat_id)
    
