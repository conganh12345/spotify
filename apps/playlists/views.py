from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from apps.cores.models import Album, Playlist, Song
from apps.albums.forms.album_create_forms import AlbumCreateForm
from apps.albums.forms.album_edit_forms import AlbumEditForm
from apps.albums.services.album_service import AlbumService
from apps.common.constants import HTTP_METHOD_POST
from apps.albums.utils import handle_album_image_upload, delete_album_image
from apps.artists.services.artist_service import ArtistService 
from datetime import date
from apps.artists.models import Artist
from apps.playlists.services.playlists_services import PlaylistService
from django.shortcuts import render, get_object_or_404
from django.http import Http404



playlist_repo = PlaylistService()

@login_required
def index(request):
    playlists = playlist_repo.get_all_playlists()
    return render(request, 'playlist/index.html', {'playlists': playlists})

def detail_playlist(request, id):
    playlist_service = PlaylistService()
    try:
        playlist = playlist_service.get_playlist_details(id)
    except Playlist.DoesNotExist:
        raise Http404("Playlist not found")
        
    return render(request, 'playlist/playlist_details.html', {'playlist': playlist})