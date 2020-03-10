from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import View, ListView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin, FormView, UpdateView

from ..forms.thread_share import ThreadShareForm
from ..forms.thread_search import ThreadSearchForm
from ..models import Thread
from ...categories.models import Category

TEMPLATE_URL = 'flyapps/threads/thread'


class HideThread(SingleObjectMixin, View):
    query_pk_and_slug = True


class LockThread(UpdateView):
    pass


class ReportThread(UpdateView):
    pass


class SearchThread(SingleObjectMixin, FormMixin, ListView):
    slug_url_kwarg = 'category_slug'
    template_name = f'{TEMPLATE_URL}/search_thread.html'
    form_class = ThreadSearchForm
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(Category.objects.all())
        self.search_query = request.GET.get('search')
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        if self.search_query:
            return self.object.threads.filter(title__icontains=self.search_query)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class ShareThread(SingleObjectMixin, FormView):
    model = Thread
    form_class = ThreadShareForm
    template_name = f'{TEMPLATE_URL}/share_thread.html'
    query_pk_and_slug = True

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(category__slug__iexact=self.kwargs['category_slug'])

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

    def get_success_url(self):
        kwargs = {
            'category_slug': self.object.category.slug,
            'pk': self.object.id,
            'slug': self.object.slug
        }
        return reverse('flyapps:threads:read_thread', kwargs=kwargs)


class UnhideThread(UpdateView):
    pass


class UnlockThread(UpdateView):
    pass


def hide_thread(request, category_slug, pk, slug):
    thread = get_object_or_404(Thread, category__slug__iexact=category_slug, pk=pk, slug__iexact=slug)
    thread.is_hidden = True
    return redirect(thread.get_absolute_url())

# def search_thread(request, category_slug):
#     category = get_object_or_404(Category, slug__iexact=category_slug)
#     is_result = False
#     results = category.threads.none()
#     if 'search' in request.GET:
#         q = request.GET.get('search')
#         results = category.threads.filter(title__icontains=q | Q(content__icontains=q))
