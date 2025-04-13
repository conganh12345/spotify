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
from apps.artist_follows.services.artist_follows_service import ArtistFollowService
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

artist_follow_repo = ArtistFollowService()
def artist_follow(request):
    if request.method == HTTP_METHOD_POST:
        try:
            data = json.loads(request.body)
            artist_id = data.get('artist_id')
            user_id = request.user.id  
            artist_follow_repo.add(user_id, artist_id)
            return JsonResponse({'success': True , 'message':'Follow thành công'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

def artist_unfollow(request,artist_id):
    if request.method == HTTP_METHOD_DELETE:
        try:
            user_id = request.user.id  
            is_success = artist_follow_repo.delete_by_user_and_artist(user_id, artist_id)
            if is_success:
                return JsonResponse({'success': True})  
            return JsonResponse({'success': False})  

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
        
        



def artist_is_followed(request, artist_id):
    if request.method == HTTP_METHOD_GET:
        try:
            user_id = request.user.id  
            followed = artist_follow_repo.get_by_user_and_artist(user_id, artist_id)
            
            if followed is None:
                return JsonResponse({'follow': False})  
            return JsonResponse({'follow': True})  

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

def get_all_artist_follows(request):
    if request.method == HTTP_METHOD_GET:
        try:
            user_id = request.user.id  
            artist_follows = artist_follow_repo.get_all_artist_follows(user_id)
            artist_data = [
                {
                    'artist_name': follow.artist.name,  
                    'artist_bio': follow.artist.bio,  
                    'artist_avatar_url': follow.artist.avatar_url,
                    'artist_avatar_url': follow.artist.avatar_url,
                    'artist_cover_url': follow.artist.cover_url,
                    'artist_genres_note': follow.artist.genres_note,
                    'artist_followed_at': follow.followed_at
                }
                for follow in artist_follows
            ]  
            return JsonResponse({'artists': artist_data})  
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)        
    

            
            
            