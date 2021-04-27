from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.views.generic.list import MultipleObjectMixin
from django.utils.translation import gettext_lazy as _

from ..forms.category import CategoryCreateForm
from ..models import Category

TEMPLATE_URL = 'blogs/category'

User = get_user_model()


class CategoryCreateView(CreateView):
    model = Category
    slug_field = 'username__iexact'
    slug_url_kwarg = 'username'
    template_name = f'{TEMPLATE_URL}/create_category.html'


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
        return redirect('sleekforum:blogs:categories:categories_list', kwargs=kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user == self.object:
            return qs.filter(owner=self.request.user, is_hidden=False)
        return qs.filter(is_hidden=True, owner=self.object)
