from django.contrib.postgres.search import SearchVector, SearchQuery, SearchHeadline
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView

from ...categories.models import Category
from ...threads.models import Thread

TEMPLATE_URL = 'search/threads'


class CategoryThreadSearch(ListView):
    model = Thread
    paginate_by = 10
    template_name = f'{TEMPLATE_URL}/search_in_category.html'

    def get(self, request, *args, **kwargs):
        self.category = request.GET.get('category')
        self.search_term = request.GET.get('search')
        if not self.category or self.category is None:
            return redirect(reverse(
                'sleekforum:search:global_thread_search'
            ) + '?search=%s' % self.search_term)
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        if self.search_term and self.category:
            category = Category.objects.get(slug__iexact=self.category)
            raw_search_query = ' OR '.join(self.search_term.split())
            query = SearchQuery(raw_search_query, search_type='raw')
            search_vector = SearchVector('title', 'content', 'posts__content')
            return qs.filter(
                category__in=category.get_descendants(include_self=True)
            ).annotate(
                search=search_vector
            ).filter(search=query)
        return qs.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['search_query'] = self.search_term
        return context


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
