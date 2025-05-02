from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from apps.cores.models import Album
from apps.albums.forms.album_create_forms import AlbumCreateForm
from apps.albums.forms.album_edit_forms import AlbumEditForm
from apps.albums.services.album_service import AlbumService
from apps.common.constants import HTTP_METHOD_POST
from apps.albums.utils import handle_album_image_upload, delete_album_image
from apps.artists.services.artist_service import ArtistService 
from datetime import date
from apps.artists.models import Artist
from apps.songs.services.song_service import SongService
album_repo = AlbumService()
artist_repo = ArtistService()
song_repo = SongService()
@login_required
def index(request):
    albums = album_repo.get_all_albums()
    return render(request, 'album/index.html', {'albums': albums})


@login_required
def create_album(request):
    today = date.today().isoformat()
    artists = artist_repo.get_all_artists()
    artists_json = list(artists.values('id','name'))
    
    if request.method == HTTP_METHOD_POST:
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            try:
                image_file = request.FILES.get('image')
                try:
                    if image_file:
                        image_url = handle_album_image_upload(image_file)
                except Exception as e:
                        messages.error(request, f'Lỗi: {str(e)}')
                album_data = form.cleaned_data
                album_data['image_url'] = image_url
                album_repo.create_album(album_data)  
                messages.success(request, 'Thêm album thành công!')
                return redirect('album_index')
            except Exception as e:
                messages.error(request, f'Lỗi: {str(e)}')
        else:
            messages.error(request, f'Đã xảy ra lỗi khi gửi biểu mẫu! {form.errors}')
    else:
        form = AlbumCreateForm()

    return render(request, 'album/create.html', {'form': form , 'artists':artists_json, 'today':today})

@login_required
def edit_album(request, album_id):
    album = album_repo.get_album_id(album_id)
    today = date.today().isoformat()
    artists = artist_repo.get_all_artists()
    artists_json = list(artists.values('id', 'name'))

    if not album:
        messages.error(request, 'Album không tồn tại.')
        return redirect('album_index')

    if request.method == HTTP_METHOD_POST:
        form = AlbumEditForm(request.POST, instance=album)
        image_file = request.FILES.get('image')

        if form.is_valid():
            try:
                album = form.save(commit=False)

                if image_file:
                    delete_album_image(album_repo.get_album_id(album_id).image_url)
                    album.image_url = handle_album_image_upload(image_file)
                else:
                    album.image_url = album_repo.get_album_id(album_id).image_url  
                album.save()
                messages.success(request, 'Cập nhật album thành công!')
                return redirect('album_index')
            except Exception as e:
                messages.error(request, f'Lỗi: {str(e)}')
        else:
            messages.error(request, 'Đã xảy ra lỗi khi gửi biểu mẫu!')
    else:
        form = AlbumEditForm(instance=album)

    return render(request, 'album/edit.html', {
        'form': form,
        'album': album,
        'today': today,
        'artists': artists_json
    })

@login_required
def delete_album(request, id):
    album = album_repo.get_album(id)
    if request.method == HTTP_METHOD_POST:
        try:
            url_image = album.image_url
            delete_album_image(url_image)
            album_repo.delete_album(id)
            return JsonResponse({'success': True}, status=200)
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Phương thức không được hỗ trợ'}, status=405)

@login_required
def detail_album(request,id):
    songs = album_repo.get_all_songs_album_id(id)
    all_songs = song_repo.get_all_songs()
    songs_json = list(all_songs.values('id','title', 'album_id'))
    print("songs_json:", songs_json)  

    return render(request, 'album/album_songs.html', {'songs': songs,'all_songs':songs_json})

@login_required
def delete_song_in_album(request, id):
    song = song_repo.get_song_id(id)
    if request.method == HTTP_METHOD_POST:
        try:
            song.album = None 
            song.save()       
            return JsonResponse({'success': True}, status=200)
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Phương thức không được hỗ trợ'}, status=405)

@login_required
def add_song_in_album(request, song_id, album_id):
    song = song_repo.get_song_id(song_id)

    if request.method == HTTP_METHOD_POST:
        try:
            if song.album is not None and song.album.id == album_id:
                return JsonResponse({'exist': True}, status=200)
            if song.album is not None and song.album.id != album_id:
                return JsonResponse({'orther_album': True}, status=200)
            new_song = song_repo.get_song_id(song_id)
            new_song.album = album_repo.get_album_id(album_id) 
            new_song.save()       
            return JsonResponse({'success': True}, status=200)
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Phương thức không được hỗ trợ'}, status=405)
