from django.db import models


class ArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_hidden=False)
