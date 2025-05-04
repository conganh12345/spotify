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
from apps.common.constants import HTTP_METHOD_PUT
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from apps.playlists_songs.services.playlists_songs_service import PlaylistSongService
from django.contrib.auth.decorators import login_required
from apps.playlists.services.playlists_services import PlaylistService
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
playlists_songs_repo = PlaylistSongService()
playlist_repo = PlaylistService()
@api_view(['GET', 'PUT','DELETE']) 
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_songs_in_playlist_id(request, playlist_id):
    if request.method == HTTP_METHOD_GET:
        try:
            songs = playlists_songs_repo.get_songs_in_playlist_id(playlist_id)
            songs_data = [{
                'id': ps.song.id,
                'title': ps.song.title,
                'duration': ps.song.duration,
                'artist': ps.song.artist.name,  
                'album': ps.song.album.title,
                'genre':ps.song.genre.name    
            } for ps in songs] 
            return JsonResponse({'success': True,'songs':songs_data})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    if request.method == HTTP_METHOD_PUT:
        try:
            data=json.loads(request.body)
            method = data.get('method')
            song_id =data.get('song_id')
            if method=='add':
                playlist_song = playlists_songs_repo.is_added_before(playlist_id=playlist_id,song_id=song_id)
                if playlist_song:
                    return JsonResponse({'success': True , 'message':'Bài hát này đã tồn tại trong playlist','result':'exist'})
                else:
                    playlists_songs_repo.add(playlist_id=playlist_id,song_id=song_id)
                    return JsonResponse({'success': True ,'result':'add' ,'message':'Thêm bài hát vào playlist thành công'})
            else:
                playlists_songs_repo.delete(playlist_id=playlist_id,song_id=song_id)
                return JsonResponse({'success': True,'result':'delete' , 'message':'Xóa 1 bài hát khỏi playlist thành công'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)    
    if request.method == HTTP_METHOD_DELETE:
        try:
            playlists_songs_repo.delete_all_songs_playlist_id(playlist_id=playlist_id)
            playlist_repo.delete(playlist_id)
            return JsonResponse({'success': True ,'message':'Xóa playlist thành công'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)               
    return JsonResponse({'error': 'Invalid request method'}, status=405)   
        
