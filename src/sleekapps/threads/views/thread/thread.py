import datetime

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Count
from django.shortcuts import redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import MultipleObjectMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from ....categories.models import Category

from ...forms.post.post import PostForm
from ...forms.thread.thread import (
    ThreadCreationForm,
    ThreadEditForm,
    QuickThreadCreationForm,
)

from ...models import Thread
from ...signals import thread_views_creator_and_updater

TEMPLATE_URL = 'threads/thread'

User = get_user_model()


class ListThread(SingleObjectMixin, ListView):
    slug_url_kwarg = 'category_slug'
    template_name = f'{TEMPLATE_URL}/index.html'
    paginate_by = 1

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(Category.objects.all())
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return self.object.threads.unhidden_threads()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.object
        return context


class CreateThread(CreateView):
    model = Category
    slug_url_kwarg = 'category_slug'
    form_class = ThreadCreationForm
    template_name = f'{TEMPLATE_URL}/create_thread.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.get_object()
        return context

    def form_valid(self, form):
        form.instance.starter = self.request.user
        form.instance.category = self.get_object()
        return super().form_valid(form)


class ReadThread(MultipleObjectMixin, SuccessMessageMixin, CreateView):
    query_pk_and_slug = True
    form_class = PostForm
    paginate_by = 1
    template_name = f'{TEMPLATE_URL}/read_thread.html'
    context_object_name = 'posts'
    success_message = _('Your post was successfully added')

    def get(self, request, *args, **kwargs):
        self.thread = self.get_object()
        self.object_list = self.get_queryset()
        return super().get(request, *args, **kwargs)

    def get_object(self):
        thread = super().get_object(
            Thread.objects.filter(
                category__slug__iexact=self.kwargs['category_slug']
            )
        )
        thread_views_creator_and_updater.send(
            self.__class__,
            request=self.request,
            thread=thread
        )
        return thread

    def post(self, request, *args, **kwargs):
        self.thread = self.get_object()
        self.object_list = self.get_queryset()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def get_queryset(self):
        return self.thread.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['thread'] = self.thread
        context['liked_by'] = [liked_by.user for liked_by in \
                               self.thread.reactions.filter_reaction_by('LIKE')]
        context['disliked_by'] = [disliked_by.user for disliked_by in \
                                  self.thread.reactions.filter_reaction_by('DISLIKE')]
        return context

    def form_valid(self, form):
        form.instance.thread = self.thread
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        msg = _('There seem to be an error with the reply your trying to submit')
        messages.error(self.request, msg)
        return super().form_invalid(form)

    def get_success_url(self):
        page_kwargs = self.request.GET.get(self.page_kwarg)
        if page_kwargs or self.get_paginate_by(self.object_list):
            kwargs = {
                'category_slug': self.kwargs['category_slug'],
                'pk': self.thread.id,
                'slug': self.thread.slug,
            }
            context = self.get_context_data()
            paginator = context['paginator']
            num_pages = paginator.num_pages
            return reverse(
                'sleekforum:threads:read_thread',
                kwargs=kwargs
            ) + '?%(page_kwargs)s=%(last_page)d' % {
                       'page_kwargs': self.page_kwarg,
                       'last_page': num_pages
                   }
        return super().get_success_url()


class EditThread(SuccessMessageMixin, UpdateView):
    model = Thread
    form_class = ThreadEditForm
    query_pk_and_slug = True
    template_name = f'{TEMPLATE_URL}/edit_thread.html'
    success_message = _('%(title)s was successfully modified')

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(
            category__slug__iexact=self.kwargs['category_slug'],
            starter=self.request.user
        )


class DeleteThread(DeleteView):
    model = Thread

    def get_success_url(self):
        kwargs = {
            'category': self.kwargs['category_slug']
        }
        return reverse('flyapps:threads:list_threads', kwargs=kwargs)


class ListNewestThread(ListView):
    model = Thread
    template_name = f'{TEMPLATE_URL}/newest_threads.html'
    paginate_by = 10
    context_object_name = 'threads'

    def get(self, request, *args, **kwargs):
        messages.info(
            self.request,
            _('Dear %(login)s, you are viewing newest \
            threads that were created 7days ago') % {
                'login': self.request.user.username if \
                    self.request.user.is_authenticated else 'guest'
            }
        )
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = QuickThreadCreationForm(user=self.request.user)
        return context

    def get_queryset(self):
        return self.model._meta.default_manager.unhidden_threads(
            created__gte=timezone.now() - datetime.timedelta(days=7)
        )


class ListTrendingThread(ListView):
    model = Thread
    template_name = f'{TEMPLATE_URL}/trending_threads.html'
    paginate_by = 10
    context_object_name = 'threads'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.annotate(
            num_of_hidden_posts=Count('posts__is_hidden')
        ).exclude(
            num_of_hidden_posts__gte=10
        ).order_by('-pin', '-num_of_hidden_posts')[:100]


@require_http_methods(['GET', 'POST'])
def create_quick_thread(request):
    if request.method == 'POST':
        form = QuickThreadCreationForm(data=request.POST, user=request.user)
        if form.is_valid():
            instance = form.save()
            messages.success(request, _('%s was successfully created' % \
                                    form.cleaned_data['title']))
            return redirect(instance.get_absolute_url())
    else:
        form = QuickThreadCreationForm(user=request.user)
