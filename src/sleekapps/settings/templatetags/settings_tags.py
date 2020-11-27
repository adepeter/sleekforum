from django import template

register = template.Library()


@register.filter
def default_if_null(configuration, default):
    if configuration == '':
        return default
