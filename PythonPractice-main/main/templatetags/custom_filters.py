from django import template

register = template.Library()


@register.filter
def get_last_part(value):
    if value:
        return value.split('/')[-1].split('.')[
            0]  # Split by '/' to get the last part, then split by '.' to remove extension
    return ''
