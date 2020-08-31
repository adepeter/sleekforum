from django import template

from violation.models import Rule


register = template.Library()

@register.filter
def rules_description(form_field):
    rule = Rule.objects.get(id=form_field.value)
    return rule.description