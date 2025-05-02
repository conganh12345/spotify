from django.db import models
from apps.artists.models import Artist 
from django.contrib.auth.models import User

class Album(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, related_name='albums')
    release_date = models.DateField(default='2025-01-01')
    image_url = models.TextField(null=True, blank=True)
    class Meta:
        db_table = 'albums'

class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'genres'
        
class Song(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, related_name='songs')
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True, related_name='songs')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    duration = models.IntegerField(null=True, blank=True)
    file_url = models.TextField(null=True, blank=True)
    duration_video = models.IntegerField(null=True, blank=True)
    video_url = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.TextField(null=True, blank=True)
    class Meta:
        db_table ='songs'

class Playlist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'playlists'

class PlaylistSong(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('playlist', 'song')
        db_table = 'playlists_songs'

class SongPlay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    played_at = models.DateTimeField(auto_now_add=True)
    plays_count = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'song_plays'
        unique_together = ('user', 'song')


class AlbumPlay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    played_at = models.DateTimeField(auto_now_add=True)
    plays_count = models.IntegerField(null=True, blank=True)
    
    class Meta:
        db_table = 'album_plays'
   
class ArtistFollow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    followed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'artist')     
        db_table = 'artist_follows'

class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    user1 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='chat_user1',db_column='user1_id')
    user2 = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='chat_user2',db_column='user2_id')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta: 
        db_table = 'chats'

class ChatMessage(models.Model):
    id = models.AutoField(primary_key=True)
    chat = models.ForeignKey(Chat, on_delete=models.SET_NULL, null=True)
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message_text = models.TextField(null=True, blank=True)
    is_read = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'chat_messages'