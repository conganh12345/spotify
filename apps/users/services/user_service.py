from django.contrib.auth.models import User, Group, Permission
from django.core.exceptions import ValidationError
from apps.users.repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.user_repo = UserRepository()
    
    def get_all_users(self):
        return self.user_repo.all()
    
    def create_user(self, form, groups):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        
        created_user = self.user_repo.create(
            username=user.username,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            password=user.password,
        )

        created_user.groups.set(groups)
        permissions = Permission.objects.filter(group__id__in=groups).distinct()
        created_user.user_permissions.set(permissions)

        return user

    def update_user(self, user, form, groups, password=None):
        updated_user = form.save(commit=False)

        if password is not None and password != '':
            updated_user.set_password(password)
        else:
            updated_user.password = user.password 

        update_data = {
            'username': updated_user.username,
            'email': updated_user.email,
            'first_name': updated_user.first_name,
            'last_name': updated_user.last_name,
            'password': updated_user.password,
        }

        self.user_repo.update(user, **update_data)

        user.groups.set(groups)
        permissions = Permission.objects.filter(group__id__in=groups).distinct()
        user.user_permissions.set(permissions)

        return user

    def delete_user(self, user_id):
        user = self.user_repo.get(user_id)
        if not user:
            raise ValidationError('Người dùng không tồn tại')
        self.user_repo.delete(user)
        return True
