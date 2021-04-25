from django.views.generic import ListView

from ..models import Category

TEMPLATE_URL = 'sleekapps/blogs'


class CategoryListView(ListView):
    model = Category
    template_name = f'{TEMPLATE_URL}/categories_list.html'

    def get_queryset(self):
        pass
