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
from apps.album_plays.services.album_plays_service import AlbumPlayService
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status

album_play_repo = AlbumPlayService()

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add(request):
    if request.method == HTTP_METHOD_POST:
        try:
            user_id = request.user.id
            data = json.loads(request.body)
            album_id = data.get('album_id')
            album_play_repo.add(user_id,album_id)
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def count_plays(request,album_id):
    if request.method == HTTP_METHOD_GET:
        try:
            count_plays = album_play_repo.count_plays(album_id)
            return JsonResponse({'success': True, 'counts':count_plays})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

            
    

            
            
            