from django import forms
from apps.artists.models import Artist 
from django.core.exceptions import ValidationError

class ArtistEditForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data['name']
        if Artist.objects.filter(name=name).exclude(id=self.instance.id).exists():
            raise ValidationError("Tên nghệ sĩ đã tồn tại.")
        if len(name) < 4:
            raise ValidationError("Tên nghệ sĩ phải dài ít nhất 4 ký tự.")
        return name