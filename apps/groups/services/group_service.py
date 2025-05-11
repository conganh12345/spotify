from django.contrib.auth.models import Group, Permission
from django.core.exceptions import ValidationError
from apps.groups.repositories.group_repository import GroupRepository

class GroupService:
    def __init__(self):
        self.group_repo = GroupRepository()

    def get_all_groups(self):
        return self.group_repo.all()

    def create_group(self, form, selected_permissions):
        group = form.save(commit=False)
        group = self.group_repo.create(
            name=group.name  
        )
        group.permissions.set(selected_permissions)
        return group

    def update_group(self, group, form, selected_permissions):
        updated_group = form.save(commit=False)
        group = self.group_repo.update(
            group,
            name=updated_group.name
        )
        group.permissions.set(selected_permissions)
        
        for user in group.user_set.all():
            # Gán quyền mới cho user
            user.user_permissions.set(group.permissions.all())
            
        return group

    def delete_group(self, group_id):
        group = self.group_repo.get(group_id)
        if not group:
            raise ValidationError('Nhóm quyền không tồn tại')
        self.group_repo.delete(group)
        return True
