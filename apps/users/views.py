from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from apps.users.forms.user_create_forms import UserCreationForm
from apps.users.forms.user_edit_forms import UserEditForm
from django.http import JsonResponse
from django.contrib.auth.models import Group, Permission
from apps.users.services.user_service import UserService
from apps.groups.services.group_service import GroupService
from django.core.exceptions import ValidationError
from apps.common.constants import HTTP_METHOD_POST

user_service = UserService()
group_service = GroupService()

@login_required
def index(request):
    users = user_service.get_all_users()
    return render(request, 'user/index.html', {'users': users})

@login_required
def create_user(request):
    groups = group_service.get_all_groups()
    if request.method == HTTP_METHOD_POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                user_service.create_user(form, request.POST.getlist('groups'))
                messages.success(request, 'Tạo người dùng thành công!')
                return redirect('user_index')
            except ValidationError as e:
                messages.error(request, f'Lỗi: {e}')
        else:
            messages.error(request, 'Đã xảy ra lỗi!')
    else:
        form = UserCreationForm()

    return render(request, 'user/create.html', {
        'form': form,
        'groups': groups
    })

@login_required
def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    groups = group_service.get_all_groups()
    if request.method == HTTP_METHOD_POST:
        form = UserEditForm(request.POST, instance=user)
        password = request.POST.get('password')  
        if form.is_valid():
            try:
                user_service.update_user(
                    user, 
                    form, 
                    request.POST.getlist('groups'), 
                    password=password
                )
                messages.success(request, 'Cập nhật người dùng thành công!')
                return redirect('user_index')
            except ValidationError as e:
                messages.error(request, f'Lỗi: {e}')
        else:
            messages.error(request, 'Đã xảy ra lỗi!')
    else:
        form = UserEditForm(instance=user)

    return render(request, 'user/edit.html', {
        'form': form,
        'user': user,
        'groups': groups
    })

@login_required
def delete_user(request, id):
    if request.method == HTTP_METHOD_POST:
        try:
            user_service.delete_user(id)
            return JsonResponse({'success': True}, status=200)
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=404)

    return JsonResponse({'error': 'Phương thức không được hỗ trợ'}, status=405)