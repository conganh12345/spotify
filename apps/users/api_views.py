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
from apps.songs.services.song_service import SongService
from apps.albums.services.album_service import AlbumService
from apps.users.services.user_service import UserService

from apps.artists.services.artist_service import ArtistService
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

song_repo = SongService()
album_repo = AlbumService()
artist_repo = ArtistService()
user_repo = UserService()

def user_list(request):
    if request.method == HTTP_METHOD_GET:
        try:
            genre_detail = genre_repo.get_genre_id(genre_id)
            songs_genre = song_repo.get_songs_by_genre_id(genre_id)

            genre_data = {
                'id': genre_detail.id,
                'name': genre_detail.name,
                'description': genre_detail.description if hasattr(genre_detail, 'description') else None,
                'created_at': genre_detail.created_at.strftime('%Y-%m-%d %H:%M:%S') if hasattr(genre_detail, 'created_at') else None
            }

            songs_data = [{
                'id': song.id,
                'title': song.title,
                'artist': {
                    'id': song.artist.id if song.artist else None,
                    'name': song.artist.name if song.artist else None
                },
                'album': {
                    'id': song.album.id if song.album else None,
                    'name': song.album.name if song.album else None
                },
                'duration': song.duration,
                'file_url': song.file_url,
                'created_at': song.created_at.strftime('%Y-%m-%d %H:%M:%S')
            } for song in songs_genre]

            result = {
                'genre': genre_data,
                'songs_genre': songs_data
            }
            return JsonResponse({'success': True, 'result': result})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
''' search  bài hát: genre,  album, ca sĩ'''
class UserViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
            
            