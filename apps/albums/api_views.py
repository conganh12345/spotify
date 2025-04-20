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
from apps.albums.services.album_service import AlbumService
from apps.artists.services.artist_service import ArtistService
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

album_repo = AlbumService()
artist_repo = ArtistService()
''' search  albums: genre,  album, ca sĩ'''
def get_albums(request, album_id):
    if request.method == HTTP_METHOD_GET:
        try:
            album_detail = album_repo.get_album_id(album_id)
            
            album_data = {
                'id': album_detail.id,
                'title': album_detail.title,
                'artist': album_detail.artist.name,
                'release_date': album_detail.release_date,                              
                'image_url': album_detail.image_url 
            }

            return JsonResponse({'success': True, 'result': album_data})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
     

    
            