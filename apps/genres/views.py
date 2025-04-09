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

genre_repo = GenreService()

@login_required
def index(request):
    genres = genre_repo.get_all_genres()
    return render(request, 'genre/index.html', {'genres': genres})


@login_required
def create_genre(request):
    if request.method == HTTP_METHOD_POST:
        form = GenreCreateForm(request.POST)
        if form.is_valid():
            try:
                genre_repo.create_genre(form)
                messages.success(request, 'Thêm thể loại thành công!')
                return redirect('genre_index')
            except Exception as e:
                messages.error(request, f'Lỗi: {str(e)}')
        else:
            messages.error(request, 'Đã xảy ra lỗi khi gửi biểu mẫu!')
    else:
        form = GenreCreateForm()

    return render(request, 'genre/create.html', {'form': form})


@login_required
def edit_genre(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)

    if request.method == HTTP_METHOD_POST:
        form = GenreEditForm(request.POST, instance=genre)
        if form.is_valid():
            try:
                genre_repo.update_genre(genre, form)
                messages.success(request, 'Cập nhật thể loại thành công!')
                return redirect('genre_index')
            except Exception as e:
                messages.error(request, f'Lỗi: {str(e)}')
        else:
            messages.error(request, 'Đã xảy ra lỗi khi gửi biểu mẫu!')
    else:
        form = GenreEditForm(instance=genre)

    return render(request, 'genre/edit.html', {
        'form': form,
        'genre': genre
    })


@login_required
def delete_genre(request, id):
    if request.method == HTTP_METHOD_POST:
        try:
            genre_repo.delete_genre(id)
            return JsonResponse({'success': True}, status=200)
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Phương thức không được hỗ trợ'}, status=405)
