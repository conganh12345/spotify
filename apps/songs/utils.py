import os
import uuid
from django.conf import settings
from mutagen import File 
from django import template

register = template.Library()

def handle_song_file_upload(file):
    ext = file.name.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    folder = 'song_files'
    path = os.path.join(settings.MEDIA_ROOT, folder, filename)

    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return f"{folder}/{filename}"


def delete_song_file(file_url):
    if file_url:
        file_path = os.path.join(settings.MEDIA_ROOT, file_url)
        if os.path.exists(file_path):
            os.remove(file_path)

def get_audio_duration(file_path):
    try:
        audio = File(file_path)
        if audio and audio.info:
            duration = audio.info.length  
            return round(duration, 2)     
    except Exception as e:
        print(f"Lỗi lấy thời lượng âm thanh: {e}")
    return 0.0

@register.filter
def format_duration(seconds):
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes}:{remaining_seconds:02d}"
