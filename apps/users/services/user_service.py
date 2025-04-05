from django.contrib.auth.models import User, Group, Permission
from django.core.exceptions import ValidationError


class UserService:

    @staticmethod
    def create_user(form, groups):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()

        selected_groups = groups
        user.groups.set(selected_groups)

        permissions = Permission.objects.filter(group__id__in=selected_groups).distinct()
        user.user_permissions.set(permissions)

        return user

    @staticmethod
    def update_user(user, form, groups, password=None):
        user = form.save(commit=False)
        if password:
            user.set_password(password)
        user.save()

        selected_groups = groups
        user.groups.set(selected_groups)

        permissions = Permission.objects.filter(group__id__in=selected_groups).distinct()
        user.user_permissions.set(permissions)

        return user

    @staticmethod
    def delete_user(user_id):
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return True
        except User.DoesNotExist:
            raise ValidationError('Người dùng không tồn tại')
