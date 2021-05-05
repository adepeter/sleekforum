from django.contrib import messages
from django.contrib.auth import get_user_model, logout, get_user
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Count, Q
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_http_methods
from django.views.generic import DetailView, UpdateView, FormView, ListView
from django.views.generic.detail import SingleObjectMixin

from ..forms.profile import UserEmailEditForm, UserProfileEditForm
from ...categories.models import Category

TEMPLATE_URL = 'users/profile'

User = get_user_model()


class UserProfile(DetailView):
    model = User
    template_name = f'{TEMPLATE_URL}/user_profile.html'

    def get_object(self):
        username = self.request.user.username
        if self.kwargs.get('username') is not None:
            username = self.kwargs['username']
        return get_object_or_404(self.model, username__iexact=username)


class UserProfileStatistics(UserProfile):
    pass


class UserPasswordChange(LoginRequiredMixin, SuccessMessageMixin, FormView):
    model = User
    form_class = PasswordChangeForm
    template_name = f'{TEMPLATE_URL}/password_change.html'
    success_url = reverse_lazy('sleekforum:users:profile:profile_password_change')
    success_message = _('Password successfully updated')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def get_object(self):
        user = get_object_or_404(
            User,
            username__iexact=self.request.user.username
        )
        return user

    def form_invalid(self, form):
        messages.error(self.request, _('An error has occurred'))
        return super().form_invalid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = get_user(self.request)
        return kwargs

    def form_valid(self, form):
        user = self.get_object()
        user.set_password(form.cleaned_data['new_password2'])
        return super().form_valid(form)


class UserProfileEdit(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserProfileEditForm
    template_name = f'{TEMPLATE_URL}/edit_profile.html'
    success_url = reverse_lazy('sleekforum:users:profile:profile_edit')
    success_message = _('Profile successfully updated')

    def form_invalid(self, form):
        messages.error(self.request, _('An error has occurred'))
        return super().form_invalid(form)

    def get_object(self):
        user = self.get_queryset()
        return user.get(username__iexact=self.request.user.username)


class UserEmailChange(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserEmailEditForm
    template_name = f'{TEMPLATE_URL}/email_change.html'
    success_url = reverse_lazy('sleekforum:users:profile:profile_email_change')
    success_message = _('E-mail successfully updated')

    def get_object(self):
        user = self.get_queryset()
        return user.get(username__iexact=self.request.user.username)

    def form_invalid(self, form):
        messages.error(self.request, _('An error has occurred'))
        return super().form_invalid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = get_user(self.request)
        return kwargs


@require_http_methods(['GET'])
def redirect_to_password_reset(request):
    """Forces a user to logout and redirect them to password reset page"""
    logout(request)
    return HttpResponsePermanentRedirect(reverse('sleekforum:users:auth:password_reset'))


class ListUserThreads(SingleObjectMixin, ListView):
    template_name = f'{TEMPLATE_URL}/threads_list.html'
    slug_field = 'username__iexact'
    slug_url_kwarg = 'username'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(User.objects.prefetch_related('threads'))
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return self.object.threads.annotate(
                unique_posters_count=Count('posts__user', distinct=True)
            )
        return self.object.threads.filter(
            is_hidden=False
        ).annotate(unique_posters_count=Count('posts__user', distinct=True))


class UserContentCategoryList(SingleObjectMixin, ListView):
    template_name = f'{TEMPLATE_URL}/categories_list.html'
    slug_field = 'username__iexact'
    slug_url_kwarg = 'username'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(User.objects.all())
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Category.objects.prefetch_related(
            'threads__starter',
            'threads__posts__user'
        ).filter(
            Q(threads__starter=self.object) | \
            Q(threads__posts__user=self.object)
        ).distinct()
