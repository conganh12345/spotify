from django import template
from apps.users.enums.user_status import UserStatus 

register = template.Library()

@register.filter
def user_status_badge(value):
    try:
        status = UserStatus.from_boolean(value)
        return {
            "text": status.text,
            "badge": status.badge
        }
    except Exception:
        return {
            "text": "Không xác định",
            "badge": "secondary"
        }
        
@register.simple_tag
def has_permission(user, perm):
    """
    Kiểm tra xem user có quyền không.
    :param user: đối tượng User
    :param perm: tên quyền (vd: 'spotify.view_song')
    :return: True nếu có quyền, False nếu không
    """
    return user.has_perm(perm)