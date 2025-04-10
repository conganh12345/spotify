from django import forms
from django.core.exceptions import ValidationError
from apps.cores.models import Album

class AlbumEditForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title' ,'artist','image_url']
    def clean_title(self):
        title = self.cleaned_data['title']
        if Album.objects.filter(title=title).exclude(pk=self.instance.pk).exists():
            raise ValidationError("Tên album đã tồn tại.")
        if len(title) < 1:
            raise ValidationError("Tên album ko được để trống.")
        return title
    def clean_artist(self):
        artist = self.cleaned_data['artist']
        if not artist:
            raise ValidationError("Phải chọn nghệ sĩ.")
        return artist
    def clean_image_url(self):
        image = self.cleaned_data.get('image_url')
        if image and image.size > 10 * 1024 * 1024:  # 10MB
            raise ValidationError("Ảnh vượt quá 10MB.")
        return image