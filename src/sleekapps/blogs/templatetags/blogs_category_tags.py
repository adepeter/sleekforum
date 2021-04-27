from django import template

from ..forms.category import CategoryEditForm

register = template.Library()


@register.inclusion_tag('blogs/_includes/edit_delete_category_popup.html', name='blogs_category_edit_delete_popup')
def category_edit_delete_popup(request, category_obj):
    form = CategoryEditForm(data=request.POST or None, instance=category_obj)
    return {
        'request': request,
        'category': category_obj,
        'form': form
    }
