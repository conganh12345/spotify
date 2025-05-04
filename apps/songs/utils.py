import os
import uuid
from django.conf import settings
from mutagen import File 
from django import template
from moviepy.editor import VideoFileClip

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

def delete_song_image(image_url):
    if image_url:
        image_path = os.path.join(settings.MEDIA_ROOT, image_url)
        if os.path.exists(image_path):
            os.remove(image_path)

def handle_song_image_upload(file):
    ext = file.name.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    folder = 'song_images'
    path = os.path.join(settings.MEDIA_ROOT, folder, filename)

    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return f"{folder}/{filename}"

def handle_video_file_upload(file):
    ext = file.name.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    folder = 'video'
    path = os.path.join(settings.MEDIA_ROOT, folder, filename)

    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return f"{folder}/{filename}"

def delete_video_file(video_url):
    if video_url:
        file_path = os.path.join(settings.MEDIA_ROOT, video_url)
        if os.path.exists(file_path):
            os.remove(file_path)

def get_video_duration(file):
    """
    Lấy thời lượng video từ file tải lên.
    Trả về thời lượng dưới dạng giây (số thực).
    """
    try:
        # Tạo thư mục temp nếu chưa tồn tại
        temp_dir = os.path.join(settings.MEDIA_ROOT, 'temp')
        os.makedirs(temp_dir, exist_ok=True)

        # Tạo tên file tạm
        ext = file.name.split('.')[-1]
        temp_filename = f"temp_{uuid.uuid4()}.{ext}"
        temp_file_path = os.path.join(temp_dir, temp_filename)

        # Ghi file tạm
        with open(temp_file_path, 'wb+') as temp_file:
            for chunk in file.chunks():
                temp_file.write(chunk)

        # Kiểm tra file tồn tại
        if not os.path.exists(temp_file_path):
            raise Exception("File tạm không được tạo.")

        # Lấy thời lượng video
        video = VideoFileClip(temp_file_path)
        duration = video.duration  # Thời lượng tính bằng giây
        video.close()

        # Xóa file tạm
        os.remove(temp_file_path)

        return round(duration, 2)
    except Exception as e:
        print(f"Lỗi lấy thời lượng video: {e}")
        return 0.0
    
@register.filter
def format_duration(value):
    if isinstance(value, int):
        minutes = value // 60
        seconds = value % 60
        return f"{minutes}:{seconds:02d}"
    return value