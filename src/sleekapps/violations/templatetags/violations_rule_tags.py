from django import template
from violation.models import Rule

register = template.Library()

@register.simple_tag
def rules_in_category(category):
    return Rule.objects.filter(category=category)
