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
            sender_id = 1
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
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])     
def get_all_messages_chat_id(request, chat_id):
    if request.method == HTTP_METHOD_POST:
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

    
   
    

            
            
            