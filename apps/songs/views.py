from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse,StreamingHttpResponse, HttpResponse, Http404
from django.core.exceptions import ValidationError
from apps.cores.models import Album
from apps.songs.forms.song_create_form import SongCreateForm
from apps.songs.forms.song_edit_form import SongEditForm
from apps.albums.services.album_service import AlbumService
from apps.genres.services.genre_service import GenreService
from apps.common.constants import HTTP_METHOD_POST
from apps.songs.utils import delete_song_image, handle_song_file_upload, delete_song_file, get_audio_duration, handle_song_image_upload, handle_video_file_upload, delete_video_file
from apps.artists.services.artist_service import ArtistService 
from apps.songs.services.song_service import SongService 
from datetime import date
from apps.artists.models import Artist
from apps.cores.models import Genre
from wsgiref.util import FileWrapper
from django.conf import settings
import os
album_repo = AlbumService()
artist_repo = ArtistService()
genre_repo = GenreService()
song_repo = SongService()

@login_required
def index(request):
    songs = song_repo.get_all_songs()
    return render(request, 'song/index.html', {'songs': songs})

@login_required
def create_song(request):
    artists = artist_repo.get_all_artists()
    artists_json = list(artists.values('id','name'))
    albums = album_repo.get_all_albums()
    albums_json = list(albums.values('id','title'))
    genres = genre_repo.get_all_genres()
    genres_json = list(genres.values('id','name'))
    if request.method == HTTP_METHOD_POST:
        form = SongCreateForm(request.POST)
        image_url = None
        file_url = None
        duration = 0
        if form.is_valid():
            try:
                image_file = request.FILES.get('image')
                if image_file:
                    image_url = handle_song_image_upload(image_file)

                audio_file = request.FILES.get('file')
                if audio_file:
                    file_url = handle_song_file_upload(audio_file)
                    duration = get_audio_duration(audio_file)

                video_file = request.FILES.get('video_file')
                if video_file:
                    video_url = handle_video_file_upload(video_file)
                    
                song_data = form.cleaned_data
                song_data['video_url'] = video_url
                song_data['file_url'] = file_url
                song_data['image_url'] = image_url
                song_data['duration'] = duration
                print("bai hat0",song_data)
                song_repo.create_song(song_data)
                messages.success(request, 'Thêm bài hát thành công!')
                return redirect('song_index')
            except Exception as e:
                messages.error(request, f'Lỗi: {str(e)}')
        else:
            messages.error(request, f'Đã xảy ra lỗi khi gửi biểu mẫu! {form.errors}') 
    else:
        form = SongCreateForm()

    return render(request, 'song/create.html', {'form': form , 'artists':artists_json, 'albums':albums_json, 'genres':genres_json})

@login_required
def edit_song(request, album_id):
    pass

@login_required
def delete_song(request, id):
    song = song_repo.get_song_id(id)
    if request.method == HTTP_METHOD_POST:
        try:
            url_image = song.image_url
            delete_song_image(url_image)
            mp3_url = song.file_url
            video_url = song.video_url
            delete_song_file(mp3_url)
            delete_video_file(video_url)
            song_repo.delete_song(id)
            return JsonResponse({'success': True}, status=200)
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Phương thức không được hỗ trợ'}, status=405)

@login_required
def edit_song(request, song_id):
    artists = artist_repo.get_all_artists()
    artists_json = list(artists.values('id','name'))
    albums = album_repo.get_all_albums()
    albums_json = list(albums.values('id','title'))
    genres = genre_repo.get_all_genres()
    genres_json = list(genres.values('id','name'))
    song = song_repo.get_song_id(song_id)
    if not song:
        messages.error(request, 'Album không tồn tại.')
        return redirect('album_index')
    if request.method == HTTP_METHOD_POST:
        form = SongEditForm(request.POST, instance=song)
        image_file = request.FILES.get('image')

        if form.is_valid():
            song_data = form.cleaned_data
            audio_file = request.FILES.get('file')
            song = form.save(commit=False)

            if image_file:
                delete_song_image(song_repo.get_song_id(song_id).image_url)
                song.image_url = handle_song_image_upload(image_file)
            else:
                song.image_url = song_repo.get_song_id(song_id).image_url  

            if audio_file:
                delete_song_file(song_repo.get_song_id(song_id).file_url)
                file_url = handle_song_file_upload(audio_file)
                duration = get_audio_duration(audio_file)
                song_data['file_url']=file_url
                song_data['duration']=duration
            else:
                song_data['file_url']=song.file_url
                song_data['duration']=song.duration
 
            video_file = request.FILES.get('video_file')
            if video_file:
                video_url = handle_video_file_upload(video_file)
                delete_video_file(song_repo.get_song_id(song_id).video_url)
                song_data['video_url'] = video_url
            else:
                song_data['video_url'] = song.video_url

            song_repo.update_song(song,song_data)
            messages.success(request, 'Update thành công!')
            return redirect('song_index')
        else:
            messages.error(request, f'Đã xảy ra lỗi khi gửi biểu mẫu! {form.errors}')  
    else:
        form = SongEditForm(instance=song)

    return render(request, 'song/edit.html', {'form': form , 'artists':artists_json, 'albums':albums_json, 'genres':genres_json , 'song':song})

@login_required
def song_file(request,id):
    song = song_repo.get_song_id(id)
    file_url = song.file_url
    image_url = song.image_url
    return render(request, 'song/mp3.html', {
        'file_url': file_url,
        'image_url': image_url
    })

@login_required
def song_video(request,id):
    song = song_repo.get_song_id(id)
    video_url = song.video_url
    return render(request, 'song/video.html', {'video_url': video_url})

def stream_song_file(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, 'song_files', filename)

    if not os.path.exists(file_path):
        raise Http404("File not found.")

    file_size = os.path.getsize(file_path)
    range_header = request.headers.get('Range', '')

    if range_header:
        try:
            start, end = range_header.replace('bytes=', '').split('-')
            start = int(start)
            end = int(end) if end else file_size - 1
        except ValueError:
            return HttpResponse(status=400)

        length = end - start + 1
        with open(file_path, 'rb') as f:
            f.seek(start)
            data = f.read(length)

        response = HttpResponse(data, status=206, content_type='video/mp4')
        response['Content-Range'] = f'bytes {start}-{end}/{file_size}'
        response['Accept-Ranges'] = 'bytes'
        response['Content-Length'] = str(length)
        return response

    # No range header: serve full file
    response = StreamingHttpResponse(FileWrapper(open(file_path, 'rb')), content_type='video/mp4')
    response['Content-Length'] = str(file_size)
    response['Accept-Ranges'] = 'bytes'
    return response