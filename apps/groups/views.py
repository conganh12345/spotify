from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from apps.groups.forms.group_create_forms import GroupCreationForm
from apps.groups.forms.group_edit_forms import GroupEditForm
from django.http import JsonResponse
from django.contrib.auth.models import Permission
from apps.groups.services.group_service import GroupService
from django.core.exceptions import ValidationError
from apps.common.constants import HTTP_METHOD_POST


@login_required
def index(request):
    groups = Group.objects.all()  
    return render(request, 'group/index.html', {'groups': groups})

@login_required
def create_group(request):
    if request.method == HTTP_METHOD_POST:
        form = GroupCreationForm(request.POST)
        if form.is_valid():
            try:
                GroupService.create_group(
                    form, 
                    request.POST.getlist('permissions')
                )
                messages.success(request, 'Tạo nhóm quyền thành công!')
                return redirect('group_index')
            except Exception as e:
                messages.error(request, f'Lỗi: {str(e)}')
        else:
            messages.error(request, 'Đã xảy ra lỗi!')
    else:
        form = GroupCreationForm()

    return render(request, 'group/create.html', {
        'form': form,
        'permissions': Permission.objects.all()
    })

@login_required
def edit_group(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    if request.method == HTTP_METHOD_POST:
        form = GroupEditForm(request.POST, instance=group)
        if form.is_valid():
            try:
                GroupService.update_group(
                    group, 
                    form, 
                    request.POST.getlist('permissions')
                )
                messages.success(request, 'Cập nhật nhóm quyền thành công!')
                return redirect('group_index')
            except Exception as e:
                messages.error(request, f'Lỗi: {str(e)}')
        else:
            messages.error(request, 'Đã xảy ra lỗi!')
    else:
        form = GroupEditForm(instance=group)

    return render(request, 'group/edit.html', {
        'form': form,
        'permissions': Permission.objects.all(),
        'group_permissions': group.permissions.all(),
        'group': group
    })

@login_required
def delete_group(request, id):
    if request.method == HTTP_METHOD_POST:
        try:
            GroupService.delete_group(id)
            return JsonResponse({'success': True}, status=200)
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=404)
    return JsonResponse({'error': 'Phương thức không được hỗ trợ'}, status=405)