from django.shortcuts import get_object_or_404

from .models import Category


class CategoryQuerysetMixin:

    def get_parent_node_obj(self):
        return get_object_or_404(
            Category,
            pk=self.kwargs['pk'],
            slug__iexact=self.kwargs['slug']
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parent_node'] = self.get_parent_node_obj()
        return context
