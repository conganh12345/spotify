from rest_framework import viewsets
from apps.cores.models import Genre
from apps.genres.serializers import GenreSerializer
from apps.common.constants import HTTP_METHOD_GET
from apps.songs.services.song_service import SongService
from apps.genres.services.genre_service import GenreService
from django.http import JsonResponse

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

song_repo = SongService()
genre_repo = GenreService()
def get_songs_by_genre_id(request, genre_id):
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
