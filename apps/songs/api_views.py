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
from apps.artists.services.artist_service import ArtistService
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

song_repo = SongService()
album_repo = AlbumService()
artist_repo = ArtistService()
''' search  bài hát: genre,  album, ca sĩ'''
def search_songs(request):
    if request.method == HTTP_METHOD_GET:
        try:
            keyword = request.GET.get('search', '').strip().lower()

            songs = []
            albums = []
            artists = []

            if keyword == '':
                songs = song_repo.get_all_songs()
                albums = album_repo.get_all_albums()
                artists = artist_repo.get_all_artists()
            else:
                songs = song_repo.search_song(keyword)
                albums = album_repo.search_album(keyword)
                artists = artist_repo.search_artist(keyword)

            
            songs_data = [{
                'id': song.id,
                'title': song.title,
                'artist': {
                    'id': song.artist.id if song.artist else None,
                    'name': song.artist.name if song.artist else None
                },
                'album': {
                    'id': song.album.id if song.album else None,
                    'title': song.album.title if song.album else None
                },
                'genre': {
                    'id': song.genre.id if song.genre else None,
                    'name': song.genre.name if song.genre else None
                },
                'duration': song.duration,
                'file_url': song.file_url,
                'image_url': song.image_url,
                'created_at': song.created_at.strftime('%Y-%m-%d %H:%M:%S')
            } for song in songs]

            
            albums_data = [{
                'id': album.id,
                'name': album.title,
                'image_url': album.image_url if album.image_url else None,
                'release_at': album.release_date
            } for album in albums]

           
            artists_data = [{
                'id': artist.id,
                'name': artist.name,
                'bio': artist.bio,
                'avatar_url': artist.avatar_url.url if artist.avatar_url else None,
                'cover_url': artist.cover_url.url if artist.cover_url else None,
                'genres_note': artist.genres_note,
                'created_at': artist.created_at.strftime('%Y-%m-%d %H:%M:%S')
            } for artist in artists]

            result_search = {
                'songs': songs_data,
                'albums': albums_data,
                'artists': artists_data
            }

            return JsonResponse({'success': True, 'result': result_search})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

            
def get_songs_id(request, song_id):
    if request.method == HTTP_METHOD_GET:
        try:
            song_detail = song_repo.get_song_id(song_id)
            
            song_data = {
                'id': song_detail.id,
                'title': song_detail.title,
                'artist': song_detail.artist.name if song_detail.artist else None,
                'duration': song_detail.duration,
                'file_url': song_detail.file_url,
                'image_url': song_detail.image_url,
                'album': song_detail.album.title if song_detail.album else None,
                'genre': song_detail.genre.name if song_detail.genre else None,
                'created_at': song_detail.created_at
            }

            return JsonResponse({'success': True, 'result': song_data})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

            