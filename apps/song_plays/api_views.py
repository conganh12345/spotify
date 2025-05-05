from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from apps.cores.models import Genre
from apps.genres.forms.genre_create_forms import GenreCreateForm
from apps.genres.forms.genre_edit_forms import GenreEditForm
from apps.genres.services.genre_service import GenreService
from apps.common.constants import HTTP_METHOD_POST
from apps.common.constants import HTTP_METHOD_GET
from apps.common.constants import HTTP_METHOD_DELETE
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from apps.song_plays.services.song_plays_service import SongPlayService
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
song_play_repo = SongPlayService()

@api_view(['POST']) 
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_song_playszzzzzz(request):
    if request.method == HTTP_METHOD_POST:
        try:
            data = json.loads(request.body)
            song_id = data.get('song_id')
            user_id = request.user.id
            print(f"Song ID: {song_id}, User ID: {user_id}")  # Đảm bảo song_id và user_id được in ra đúng

            song_play_repo.add(user_id,song_id)
            
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


def count_plays(request,song_id):
    if request.method == HTTP_METHOD_GET:
        try:
            count_plays = song_play_repo.count_plays(song_id)
            return JsonResponse({'success': True, 'counts':count_plays})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

            
    

            
            
            