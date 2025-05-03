from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from apps.users.repositories.user_repository import UserRepository
from apps.artists.repositories.artist_repository import ArtistRepository
from apps.genres.repositories.genre_repository import GenreRepository
from apps.songs.repositories.song_repository import SongRepository
from apps.albums.repositories.album_repository import AlbumRepository
from apps.song_plays.repositories.song_plays_repository import SongPlayRepository


song_play_repo = SongPlayRepository()
genre_repo = GenreRepository()
user_repo = UserRepository()
artist_repo = ArtistRepository()
album_repo = AlbumRepository()
song_repo = SongRepository()

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('/admin') 
    user_count = user_repo.count_all_user()
    artist_count = artist_repo.count_all_artist()
    genre_count = genre_repo.count_all_genre()
    album_count = album_repo.count_all_album()
    song_count = song_repo.count_all_song()

    context = {
        'user_count': user_count,
        'artist_count': artist_count,
        'genre_count': genre_count,
        'song_count': song_count,
        'album_count': album_count,
    }        
    return render(request, 'dashboard/index.html', context)


def get_song_plays(request):
    play_stats = song_play_repo.get_play_stats_last_15_days()
    return JsonResponse(play_stats)