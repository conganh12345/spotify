import os
import uuid
from django.conf import settings

def handle_album_image_upload(file):
    ext = file.name.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    folder = 'album_images'
    path = os.path.join(settings.MEDIA_ROOT, folder, filename)

    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return f"{folder}/{filename}"
def delete_album_image(image_url):
    if image_url:
        image_path = os.path.join(settings.MEDIA_ROOT, image_url)
        if os.path.exists(image_path):
            os.remove(image_path)