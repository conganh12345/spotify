from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserEditForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput, 
        min_length=8, 
        label="Mật khẩu", 
        required=False  
    )
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_username(self):
        username = self.cleaned_data['username']
        if (username != self.instance.username and 
            User.objects.filter(username=username).exclude(pk=self.instance.pk).exists()):
            raise ValidationError("Tên đăng nhập đã tồn tại.")
        if len(username) < 4:
            raise ValidationError("Tên đăng nhập phải dài ít nhất 4 ký tự.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if (email != self.instance.email and 
            User.objects.filter(email=email).exclude(pk=self.instance.pk).exists()):
            raise ValidationError("Email này đã được sử dụng.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password != '':
            user.set_password(password)
        if commit:
            user.save()
        return user