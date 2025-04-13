from django.core.exceptions import ValidationError
from apps.artists.repositories.artist_repository import ArtistRepository

class ArtistService:
    def __init__(self):
        self.artist_repo = ArtistRepository()

    def get_all_artists(self):
        return self.artist_repo.all()

    def create_artist(self, form):
        artist = form.save()
        return artist

    def update_artist(self, artist, form):
        artist = form.save()
        return artist

    def delete_artist(self, artist_id):
        artist = self.artist_repo.get(artist_id)
        self.artist_repo.delete(artist)
        return True
    
    def search_artist(self, keyword):
        return self.artist_repo.search_artist(keyword)
    
