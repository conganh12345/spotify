from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from apps.cores.models import Chat
from apps.chats.services.chat_service import ChatService
from apps.chat_messages.services.chat_message_service import ChatMessageRepository
from django.views.decorators.csrf import csrf_exempt

from apps.common.constants import HTTP_METHOD_POST
from apps.common.constants import HTTP_METHOD_GET
from apps.common.constants import HTTP_METHOD_DELETE
from apps.common.constants import HTTP_METHOD_PUT
from django.utils.timezone import localtime

chat_service = ChatService()
chat_message_service = ChatMessageRepository()
@login_required
def index(request):
    chats = chat_service.get_all_chats()
    return render(request, 'chat/index.html', {'chats': chats})

@login_required
def detail_chat(request, id):
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
        return JsonResponse(chat_messages_data, safe=False)
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
        return render(request, 'chat/detail.html', {
            'chat': chat_json,
            'chat_messages': chat_messages_data
        })
@csrf_exempt
def delete_chat(request, id):
    if request.method == HTTP_METHOD_POST:
        try:
            chat_message_service.delete_all_messages_by_chat_id(id)
            return JsonResponse({'success': True}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)





    

        