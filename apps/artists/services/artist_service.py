from django.core.exceptions import ValidationError
from apps.artists.repositories.artist_repository import ArtistRepository

class ArtistService:
    def __init__(self):
        self.artist_repo = ArtistRepository()

    def get_all_artists(self):
        return self.artist_repo.all()

    def create_artist(self, form, selected_permissions):
        artist = form.save(commit=False)
        artist = self.artist_repo.create(
            name=artist.name  
        )
        artist.permissions.set(selected_permissions)
        return artist

    def update_artist(self, artist, form, selected_permissions):
        updated_artist = form.save(commit=False)
        artist = self.artist_repo.update(
            artist,
            name=updated_artist.name
        )
        artist.permissions.set(selected_permissions)
        return artist

    def delete_artist(self, artist_id):
        artist = self.artist_repo.get(artist_id)
        if not artist:
            raise ValidationError('Nhóm quyền không tồn tại')
        self.artist_repo.delete(artist)
        return True
