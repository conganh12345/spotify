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
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
chat_repo = ChatService()
chat_message_repo = ChatMessageService()
@api_view(['GET', 'POST']) 
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def chat(request):
    if request.method == HTTP_METHOD_POST:
        try:
            data = json.loads(request.body)
            user2_id = data.get('user2_id')
            user1_id = request.user.id
            chat_repo.add(user1_id=user1_id,user2_id=user2_id)
            return JsonResponse({'success': True , 'message':'Follow thành công'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    if request.method == HTTP_METHOD_GET:
        try:
            user_id = request.user.id
            chats = chat_repo.get_all_chats_by_userid(user_id)
            last_messages = chat_message_repo.get_chats_with_last_message(chats)
            result = []
            for last_message in last_messages:
                if last_message is not None:
                    chat = last_message.chat  
                    result.append({
                        'chat_id': chat.id,
                        'user1_id': chat.user1.id if chat.user1 else None,
                        'user2_id': chat.user2.id if chat.user2 else None,
                        'created_at': chat.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                        'user1_name':chat.user1.username,
                        'user2_name':chat.user2.username,
                        'chat_message': {
                            'id': last_message.id,
                            'message_text': last_message.message_text,
                            'is_read': last_message.is_read,
                            'created_at': last_message.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                            'chat_id': chat.id,
                            'sender_id': last_message.sender.id if last_message.sender else None
                        }
                    })
            return JsonResponse({'success': True, 'result': result})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


    return JsonResponse({'error': 'Invalid request method'}, status=405)            

   
    

            
            
            