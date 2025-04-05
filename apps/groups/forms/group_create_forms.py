from django import forms
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError

class GroupCreationForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']

    def clean_name(self):
        name = self.cleaned_data['name']
        if Group.objects.filter(name=name).exists():
            raise ValidationError("Tên nhóm quyền đã tồn tại.")
        if len(name) < 4:
            raise ValidationError("Tên nhóm quyền phải dài ít nhất 4 ký tự.")
        return name