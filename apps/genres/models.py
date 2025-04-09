from django.db import models

# Create your models here.
'''
class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'genres'
'''