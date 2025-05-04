from django import forms
from django.contrib.auth.models import Group, User
from django.core.exceptions import ValidationError

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, label="Mật khẩu")
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("Tên đăng nhập đã tồn tại.")
        if len(username) < 4:
            raise ValidationError("Tên đăng nhập phải dài ít nhất 4 ký tự.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email này đã được sử dụng.")
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        if not password:
            raise ValidationError("Mật khẩu là bắt buộc khi tạo mới.")
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_superuser = True
        user.set_password(self.cleaned_data['password'])  
        if commit:
            user.save()
        return user