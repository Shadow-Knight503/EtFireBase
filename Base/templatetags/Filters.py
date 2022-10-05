from django import template

register = template.Library()


@register.filter
def get_index(value, arg):
    return value[int(arg)]

