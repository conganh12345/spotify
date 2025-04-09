from django.core.exceptions import ValidationError
from apps.genres.repositories.genre_repository import GenreRepository

class GenreService:
    def __init__(self):
        self.genre_repo = GenreRepository()

    def get_all_genres(self):
        return self.genre_repo.all()

    def create_genre(self, form):
        genre_data = form.cleaned_data
        genre = self.genre_repo.create(**genre_data)
        return genre

    def update_genre(self, genre, form):
        updated_data = form.cleaned_data
        updated_genre = self.genre_repo.update(genre, **updated_data)
        return updated_genre

    def delete_genre(self, genre_id):
        genre = self.genre_repo.get(genre_id)
        if not genre:
            raise ValidationError('Thể loại không tồn tại')
        self.genre_repo.delete(genre)
        return True
