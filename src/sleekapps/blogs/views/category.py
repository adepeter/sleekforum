from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Count
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, UpdateView
from django.views.generic.list import MultipleObjectMixin
from rest_framework.reverse import reverse

from ..forms.category import CategoryCreateForm, CategoryEditForm
from ..models import Category

TEMPLATE_URL = 'blogs/category'

User = get_user_model()


class CategoryEditDeleteView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Category
    form_class = CategoryEditForm
    slug_field = 'slug__iexact'
    slug_url_kwarg = 'slug'
    template_name = f'{TEMPLATE_URL}/edit_delete_category.html'
    success_message = '%(name)s was successfully modified'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner__username__iexact=self.request.user.username)

    def get_success_url(self):
        kwargs = {
            'username': self.object.owner.username
        }
        return reverse('sleekforum:blogs:categories:categories_list_create', kwargs=kwargs)


class CategoryListCreateView(MultipleObjectMixin, SuccessMessageMixin, CreateView):
    model = Category
    form_class = CategoryCreateForm
    slug_field = 'username__iexact'
    slug_url_kwarg = 'username'
    template_name = f'{TEMPLATE_URL}/categories_list.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object_list = self.get_queryset()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.get_object()
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def get_object(self, queryset=User.objects.all()):
        return super().get_object(queryset=queryset)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object_list = self.get_queryset()
        return super().post(request, *args, **kwargs)

    def form_invalid(self, form):
        messages.error(self.request, _('There is an error with your submitted data'))
        return super().form_invalid(form)

    def get_success_url(self):
        obj = self.object
        kwargs = {
            'username': obj.owner.username
        }
        return redirect('sleekforum:blogs:categories:categories_list_create', kwargs=kwargs)

    def get_queryset(self):
        qs = super().get_queryset().annotate(
            num_of_articles=Count('articles'),
            num_of_comments=Count('articles__blog_comments')
        )
        if self.request.user == self.object:
            return qs.filter(owner=self.object)
        return qs.filter(is_hidden=False, owner=self.object)


@require_POST
def delete_category(request, username, category):
    category = Category.objects.filter(owner__username__iexact=username, name=category.name)
    is_deleted = category.delete()
    if is_deleted:
        messages.success(request, _('%s was successfully deleted' % category.name))
    else:
        messages.info(request, _('%s could not be deleted.\
        Probably doesn\'t exist or don\'t possess delete permissions' % category.name))
    return reverse()
