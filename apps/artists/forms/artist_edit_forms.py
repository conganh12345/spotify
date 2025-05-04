from django import forms
from apps.artists.models import Artist 
from django.core.exceptions import ValidationError

class ArtistEditForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'bio', 'avatar_url', 'cover_url']

    def clean_name(self):
        name = self.cleaned_data['name']
        if Artist.objects.filter(name=name).exclude(id=self.instance.id).exists():
            raise ValidationError("Tên nghệ sĩ đã tồn tại.")
        if not name:
            raise ValidationError("Tên nghệ sĩ không được để trống.")
        if len(name) < 4:
            raise ValidationError("Tên nghệ sĩ phải dài ít nhất 4 ký tự.")
        return name
    
    def clean_bio(self):
        bio = self.cleaned_data.get('bio')
        if not bio:
            raise ValidationError("Tiểu sử không được để trống.")
        if bio and len(bio) > 500:
            raise ValidationError("Tiểu sử không được dài quá 500 ký tự.")
        return bio

    def clean_avatar_url(self):
        avatar_url = self.cleaned_data.get('avatar_url')
        if not avatar_url:
            raise ValidationError("Ảnh đại diện không được để trống.")
        return avatar_url

    def clean_cover_url(self):
        cover_url = self.cleaned_data.get('cover_url')
       
        return cover_url