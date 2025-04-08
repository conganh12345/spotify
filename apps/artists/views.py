from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from apps.artists.models import Artist
from apps.artists.forms.artist_create_forms import ArtistCreationForm
from apps.artists.forms.artist_edit_forms import ArtistEditForm
from apps.artists.services.artist_service import ArtistService
from apps.common.constants import HTTP_METHOD_POST

artist_repo = ArtistService()

@login_required
def index(request):
    artists = artist_repo.get_all_artists()
    return render(request, 'artist/index.html', {'artists': artists})


@login_required
def create_artist(request):
    if request.method == HTTP_METHOD_POST:
        form = ArtistCreationForm(request.POST)
        if form.is_valid():
            try:
                artist_repo.create_artist(form)
                messages.success(request, 'Tạo nghệ sĩ thành công!')
                return redirect('artist_index')
            except Exception as e:
                messages.error(request, f'Lỗi: {str(e)}')
        else:
            messages.error(request, 'Đã xảy ra lỗi khi gửi biểu mẫu!')
    else:
        form = ArtistCreationForm()

    return render(request, 'artist/create.html', {'form': form})


@login_required
def edit_artist(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)

    if request.method == HTTP_METHOD_POST:
        form = ArtistEditForm(request.POST, instance=artist)
        if form.is_valid():
            try:
                artist_repo.update_artist(artist, form)
                messages.success(request, 'Cập nhật nghệ sĩ thành công!')
                return redirect('artist_index')
            except Exception as e:
                messages.error(request, f'Lỗi: {str(e)}')
        else:
            messages.error(request, 'Đã xảy ra lỗi khi gửi biểu mẫu!')
    else:
        form = ArtistEditForm(instance=artist)

    return render(request, 'artist/edit.html', {
        'form': form,
        'artist': artist
    })


@login_required
def delete_artist(request, artist_id):
    if request.method == HTTP_METHOD_POST:
        try:
            artist_repo.delete_artist(artist_id)
            return JsonResponse({'success': True}, status=200)
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Phương thức không được hỗ trợ'}, status=405)
