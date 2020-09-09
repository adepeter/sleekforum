from django.contrib.postgres.search import SearchVector, SearchQuery, SearchHeadline
from django.views.generic import ListView
from django.views.generic.edit import FormMixin

from ...threads.models import Thread

TEMPLATE_URL = 'search/threads'


class CategoryThreadSearch:
    pass


class GlobalThreadSearch(ListView):
    model = Thread
    paginate_by = 10
    template_name = f'{TEMPLATE_URL}/search.html'

    def get(self, request, *args, **kwargs):
        self.search_query = request.GET.get('search')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        if self.search_query is not None:
            search_term = self.search_query
            websearch_query = ' OR '.join(search_term.split())
            query = SearchQuery(websearch_query, search_type='websearch')
            search_vector = SearchVector('title', 'content', 'posts__content')
            return qs.annotate(search=search_vector).filter(search=query)
        return qs.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.search_query
        return context
