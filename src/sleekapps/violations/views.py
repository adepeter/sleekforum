from django.shortcuts import render
from violation.behaviours import BaseRuleModelMixin
from violation.models import Rule

from ..cores.utils.choice import Choicify
from .exceptions import RuleForCategoryDoesNotExist

TEMPLATE_URL = 'violations/rules'

choicify_categories = Choicify(BaseRuleModelMixin.CATEGORY_CHOICES)
categories = choicify_categories.to_dict()


def category(request):
    template_name = f'{TEMPLATE_URL}/categories_list.html'
    context = {'categories': categories}
    return render(request, template_name, context=context)


def rules(request, category):
    template_name = f'{TEMPLATE_URL}/rules_list.html'
    if category not in categories:
        raise RuleForCategoryDoesNotExist('No rule can be display for the specified category')
    rules = Rule.objects.rules_in(category)
    context = {
        'category': category,
        'rules': rules
    }
    return render(request, template_name, context)
