from django import forms
from django.core.exceptions import ValidationError
from apps.cores.models import Genre
class GenreCreateForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name' ,'description']
    def clean_name(self):
        name = self.cleaned_data['name']
        if Genre.objects.filter(name=name).exists():
            raise ValidationError("Tên tthể loại đã tồn tại.")
        if len(name) < 3:
            raise ValidationError("Tên thể loại phải có ít nhất 3 ký tự.")
        return name
    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 1:
            raise ValidationError("Không được để trống phần mô tả.")
        return description