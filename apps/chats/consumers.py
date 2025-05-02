import json
from channels.generic.websocket import AsyncWebsocketConsumer
import requests
import asyncio

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_id = self.scope['url_route']['kwargs']['chat_id']
        self.room_group_name = f'chat_{self.chat_id}'  

        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    async def receive(self, text_data):
        data = json.loads(text_data)
        command = data.get('command')
        if command =='delete_chat':
            await self.delete_chat(data)
            
        elif command == 'delete_message':
            await self.delete_message(data)
        else:
            message_text = data['message_text']
            sender_id = data['sender_id']
            chat_id = data['chat_id']
            chat_id = self.chat_id
            api_url = f'http://localhost:8000/api/chats/{chat_id}/messages/'
            headers = {'Content-Type': 'application/json'}
            payload = {
                'message_text': message_text,
                'sender_id': sender_id,
                'chat_id':chat_id,
            }
            response = await asyncio.to_thread(requests.post, api_url, json=payload, headers=headers)
            print(f"Status Code: {response.status_code}")
            if response.status_code == 201:
                response_data = response.json()
                m = response_data['new_message']
                await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message', 
                    'message_text': m['message_text'],
                    'sender_id': m['sender_id'],
                    'chat_id':m['chat_id'],
                    'created_at':m['created_at'],
                    'is_read':m['is_read'],
                    'id':m['id'],
                    'time':m['time'],
                    'date':m['date']
                }
                )
                print("Tin nhắn đã được gửi thành công.")

            else:
                print("Lỗi khi gửi tin nhắn:")
                print(f"Response text: {response.text}")
                try:
                    # Cố gắng đọc dữ liệu JSON nếu có
                    response_data = response.json()
                    print("Thông tin lỗi từ server:", response_data)
                except ValueError:
                    print("Phản hồi không phải là JSON.")
        
    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'message_type': 'create_chat_response',
            'message_text': event['message_text'],
            'sender_id': event['sender_id'],
            'chat_id':event['chat_id'],
            'is_read':event['is_read'],
            'created_at':event['created_at'],
            'id':event['id'],
            'time':event['time'],
            'date':event['date']
        }))
    async def delete_chat(self,data):
        chat_id = data['chat_id']
        api_url = f'http://localhost:8000/chat/delete/{chat_id}'
        headers = {'Content-Type': 'application/json'}
        response = await asyncio.to_thread(requests.post, api_url, headers=headers)
        if response.status_code ==201:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'delete_chat_response', 
                    'success':True
                }
                )
        else:
            print('Lỗi khi xóa tin nhắn')
    async def delete_chat_response(self,event):
        await self.send(text_data=json.dumps({
            'message_type': 'delete_chat_response',
            'success': event['success'],
        }))
    async def delete_message(self,data):
        pass
    