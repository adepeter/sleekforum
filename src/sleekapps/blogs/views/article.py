from django.contrib.auth import get_user_model
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

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
