from django.db import models

class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,blank=True,null=True)
    bio = models.TextField(null=True,blank=True)
    avatar_url = models.ImageField(upload_to='images/', blank=True, null=True)
    cover_url = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    genres_note = models.CharField(max_length=100,blank=True,null=True)
    class Meta:
        db_table='artists'