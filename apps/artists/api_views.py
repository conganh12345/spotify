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
from apps.cores.models import Artist
from apps.cores.models import Song

song_repo = SongService()
album_repo = AlbumService()
artist_repo = ArtistService()

     
def get_artists_id(request, artist_id):
    if request.method == HTTP_METHOD_GET:
        try:
            artist_detail = artist_repo.get_artist_id(artist_id)
            # songs = artist_detail.songs.all()
            # albums = artist_detail.albums.all()
            
            # song_list = []
            # for song in songs:
            #     song_list.append({
            #         'id': song.id,
            #         'title': song.title,
            #         'artist': song.artist.name if song.artist else None,
            #         'genre': song.genre.name if song.genre else None,
            #         'duration': song.duration,
            #         'file_url': song.file_url
            #     })

            # album_list = []
            # for album in albums:
            #     album_list.append({
            #         'id': album.id,
            #         'title': album.title,
            #         'artist': album.artist.name if song.artist else None,
            #         'genre': album.genre.name if song.genre else None,
            #         'duration': album.duration,
            #         'file_url': album.file_url
            #     })
            
            artist_data = {
                'id': artist_detail.id,
                'name': artist_detail.name,
                'bio': artist_detail.bio,
                'avatar_url': artist_detail.avatar_url.url if artist_detail.avatar_url else None,
                'cover_url': artist_detail.cover_url.url if artist_detail.cover_url else None,
                'created_at': artist_detail.created_at,
                'genres_note': artist_detail.genres_note,
                # 'songs': song_list, 
                # 'albums': album_list
            }

            return JsonResponse({'success': True, 'result': artist_data})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def get_all_artists(request):
    try:
        artists = artist_repo.get_all_artists()  
        all_artists_data = []

        for artist in artists:
            # songs = Song.objects.filter(album=album)

            # song_list = []
            # for song in songs:
            #     song_list.append({
            #         'id': song.id,
            #         'title': song.title,
            #         'artist': song.artist.name if song.artist else None,
            #         'genre': song.genre.name if song.genre else None,
            #         'duration': song.duration,
            #         'file_url': song.file_url,
            #     })

            artist_data = {
                'id': artist.id,
                'name': artist.name,
                'bio': artist.bio,
                'avatar_url': artist.avatar_url.url if artist.avatar_url else None,
                'cover_url': artist.cover_url.url if artist.cover_url else None,
                'created_at': artist.created_at,
                'genres_note': artist.genres_note,
                # 'songs': song_list, 
                # 'albums': album_list
            }

            all_artists_data.append(artist_data)

        return JsonResponse({'success': True, 'result': all_artists_data})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


