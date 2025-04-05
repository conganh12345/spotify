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