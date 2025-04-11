from django.core.exceptions import ValidationError
from apps.albums.repositories.album_repository import AlbumRepository

class AlbumService:
    def __init__(self):
        self.album_repo = AlbumRepository()
    def get_album(self, album_id):
        return self.album_repo.get(album_id)
    
    def get_album_id(self,id):
        return self.album_repo.get_album_id(id)
    
    
    def get_all_albums(self):
        return self.album_repo.get_all_albums()

    def create_album(self, album_data):
         album = self.album_repo.create(**album_data)
         return album

    def update_album(self, album,  album_data):
        album_updated=self.album_repo.update(album, ** album_data)
        return album_updated

    def delete_album(self, album_id):
        album = self.album_repo.get(album_id)
        if not album:
            raise ValidationError('Album không tồn tại')
        self.album_repo.delete(album)
        return True

    def get_all_songs_album_id(self,id):
        return self.album_repo.get_all_songs_album_id(id)