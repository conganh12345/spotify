from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from apps.cores.models import Genre
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
from apps.cores.models import Album
from apps.cores.models import Song
from apps.songs.utils import format_duration

song_repo = SongService()
album_repo = AlbumService()
artist_repo = ArtistService()

     
def get_albums_id(request, album_id):
    if request.method == HTTP_METHOD_GET:
        try:
            album_detail = album_repo.get_album_id(album_id)
            songs = album_detail.songs.all()

            song_list = []
            for song in songs:
                song_list.append({
                    'id': song.id,
                    'title': song.title,
                    'artist': song.artist.name if song.artist else None,
                    'genre': song.genre.name if song.genre else None,
                    'duration_video': format_duration(song.duration_video),
                    'video_url': song.video_url,
                    'image_url': song.image_url,
                })

            album_data = {
                'id': album_detail.id,
                'title': album_detail.title,
                'artist': album_detail.artist.name if album_detail.artist else None,
                'release_date': album_detail.release_date,
                'image_url': album_detail.image_url,
                'songs': song_list  
            }

            return JsonResponse({'success': True, 'result': album_data})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def get_all_albums(request):
    try:
        albums = album_repo.get_all_albums()  
        all_albums_data = []

        for album in albums:
            songs = Song.objects.filter(album=album)

            song_list = []
            for song in songs:
                song_list.append({
                    'id': song.id,
                    'title': song.title,
                    'artist': song.artist.name if song.artist else None,
                    'genre': song.genre.name if song.genre else None,
                    'duration': format_duration(song.duration_video),
                    'video_url': song.video_url,
                })

            album_data = {
                'id': album.id,
                'title': album.title,
                'artist': album.artist.name if album.artist else None,
                'release_date': album.release_date,
                'image_url': album.image_url,
                'songs': song_list
            }

            all_albums_data.append(album_data)

        return JsonResponse({'success': True, 'result': all_albums_data})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


