# apps/songs/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def duration_format(value):
    if isinstance(value, int):
        minutes = value // 60
        seconds = value % 60
        return f"{minutes}:{seconds:02d}"
    return value
