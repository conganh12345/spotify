from django.contrib.auth.models import Group, Permission
from django.core.exceptions import ValidationError, ObjectDoesNotExist

class GroupService:

    @staticmethod
    def create_group(form, selected_permissions):
        group = form.save()
        group.permissions.set(selected_permissions)
        group.save()
        return group

    @staticmethod
    def update_group(group, form, selected_permissions):
        group = form.save()
        group.permissions.set(selected_permissions)
        group.save()
        return group

    @staticmethod
    def delete_group(group_id):
        try:
            group = Group.objects.get(id=group_id)
            group.delete()
        except Group.DoesNotExist:
            raise ValidationError('Nhóm quyền không tồn tại')

