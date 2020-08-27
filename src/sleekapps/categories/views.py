from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.urls import reverse

from ..threads.models import Thread
from .models import Category
from .viewmixins import CategoryQuerysetMixin


TEMPLATE_URL = 'categories'


class RootCategoryListView(ListView):
    template_name = f'{TEMPLATE_URL}/index.html'
    model = Category
    context_object_name = 'categories'


class ChildrenCategoryListView(CategoryQuerysetMixin, ListView):
    template_name = f'{TEMPLATE_URL}/subcategories.html'
    context_object_name = 'subcategories'

    def get_queryset(self):
        parent_node_obj = self.get_parent_node_obj()
        return parent_node_obj.get_children()

    def dispatch(self, request, *args, **kwargs):
        """Loads if category does not contain thread(s)
        and is also not locked else redirects to threadlist section
        """
        obj = self.get_parent_node_obj()
        if obj.threads.exists() or not obj.is_lock:
            kwargs = {
                'category_id': obj.id,
                'category_slug': obj.slug
            }
            return HttpResponseRedirect(
                reverse('sleekforum:threads:list_threads', kwargs=kwargs)
            )
        return super().dispatch(request, *args, **kwargs)


class ListDescendantCategoryThread(CategoryQuerysetMixin, ListView):
    """
    Returns all threads within a parent category
    """
    model = Thread
    template_name = f'{TEMPLATE_URL}/thread_list.html'
    context_object_name = 'threads'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        parent_node_obj = self.get_parent_node_obj()
        qs = qs.filter(
            category__in=parent_node_obj.get_descendants(include_self=True),
            is_hidden=False,
        )
        return qs