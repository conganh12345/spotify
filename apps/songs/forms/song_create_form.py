from django import forms
from django.core.exceptions import ValidationError
from apps.cores.models import Song
class SongCreateForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title' ,'artist','file_url','album','genre','duration', 'video_url', 'duration_video']
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 1:
            raise ValidationError("Tên song ko được để trống.")
        return title
    album = forms.ModelChoiceField(
        queryset=Song._meta.get_field('album').remote_field.model.objects.all(),
        required=False
    )