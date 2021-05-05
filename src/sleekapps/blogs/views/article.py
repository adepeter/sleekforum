from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import MultipleObjectMixin

from ..models import Article

TEMPLATE_URL = 'blogs/article'

User = get_user_model()


class ArticlesByUserListView(SingleObjectMixin, ListView):
    model = Article
    slug_url_kwarg = 'username'
    slug_field = 'username__iexact'
    query_pk_and_slug = True
    paginate_by = 1
    template_name = f'{TEMPLATE_URL}/articles_list.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(User.objects.all())
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        obj = self.object
        if obj == self.request.user:
            return obj.blog_articles.all()
        return qs.filter(is_hidden=False)


class ArticleByUserReadView(MultipleObjectMixin, SuccessMessageMixin, CreateView):
    model = Article
    template_name = f'{TEMPLATE_URL}/read_article.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(is_hidden=False)


class ArticleDetailView(DetailView):
    model = Article
    template_name = f'{TEMPLATE_URL}/read_article.html'


class UserArticlesByCategoryView(SingleObjectMixin, ListView):
    template_name = f'{TEMPLATE_URL}/user_articles_by_category.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super().get_object(queryset=queryset)

    def get_queryset(self):
        return self.object.articles.all()
