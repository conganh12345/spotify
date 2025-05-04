from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from apps.common.constants import HTTP_METHOD_POST
from apps.common.constants import HTTP_METHOD_GET
from apps.common.constants import HTTP_METHOD_DELETE
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from apps.chats.services.chat_service import ChatService
from apps.chat_messages.services.chat_message_service import ChatMessageService
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.timezone import localtime
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
chat_repo = ChatService()
chat_message_repo = ChatMessageService()
'''
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
'''
@csrf_exempt
def create_message(request,chat_id):
    if request.method == HTTP_METHOD_POST:
        try:
            data = json.loads(request.body)
            message_text = data.get('message_text')
            sender_id = data.get('sender_id')
            new_message = chat_message_repo.create_message(chat_id=chat_id,message_text=message_text,sender_id=sender_id)
            new_message_dict = {
                'message_text': new_message.message_text,
                'is_read': new_message.is_read,
                'created_at': new_message.created_at,
                'chat_id':new_message.chat_id,
                'sender_id':new_message.sender_id,
                'id':new_message.id,
                'time': localtime(new_message.created_at).strftime('%H:%M'),
                'date': localtime(new_message.created_at).strftime('%d-%m-%Y'),
            }
            return JsonResponse({'success': True , 'message':'Tạo message thành công','new_message':new_message_dict}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)       
'''
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])     
def get_all_messages_chat_id(request, chat_id):
    if request.method == HTTP_METHOD_GET:
        try:
            chat_messages = chat_message_repo.get_all_messages_chat_id(chat_id)
            result = []
            for message in chat_messages:
                result.append({
                    'id': message.id,
                    'message_text': message.message_text,
                    'is_read': message.is_read,
                    'created_at': message.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    'chat_id': message.chat.id if message.chat else None,
                    'sender_id': message.sender.id if message.sender else None,
                    
                })
            return JsonResponse({'success': True, 'result': result})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
'''
chat_service = ChatService()
chat_message_service = ChatMessageService()
@api_view(['GET']) 
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def detail_chat(request, id):
    if request.method == HTTP_METHOD_GET:
        last_id = request.GET.get('last_id')
        chat = chat_service.get_chat_by_id(id)
        if last_id:
            chat_messages = chat_message_service.get_all_messages_chat_id_after(id, last_id)
            chat_messages_data = [
                {
                    'message_text': c.message_text,
                    'is_read': c.is_read,
                    'created_at': c.created_at,
                    'sender_id': c.sender_id,
                    'id': c.id,
                    'time': localtime(c.created_at).strftime('%H:%M'),
                    'date': localtime(c.created_at).strftime('%d-%m-%Y'),
                }
                for c in chat_messages
            ]
            return JsonResponse({'success': True,'messages':chat_messages_data})
        else:
            chat_messages = chat_message_service.get_all_messages_chat_id_first(id)
            chat_json = {
                'chat_id': id,
                'user1_username': chat.user1.username,
                'user2_username': chat.user2.username,
                'user1_id': chat.user1.id,
                'user2_id': chat.user2.id
            }
            chat_messages_data = [
                {
                    'message_text': c.message_text,
                    'is_read': c.is_read,
                    'created_at': c.created_at,
                    'sender_id': c.sender_id,
                    'id': c.id,
                    'time': localtime(c.created_at).strftime('%H:%M'),
                    'date': localtime(c.created_at).strftime('%d-%m-%Y'),
                }
                for c in chat_messages
            ]
            return JsonResponse({'success': True, 'chat': chat_json,
                'chat_messages': chat_messages_data})

   
    

            
            
            