from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Article


@receiver(pre_save, sender=Article)
def mark_new_blog_as_draft(sender, instance, **kwargs):
    if not instance.content:
        instance.completion_status = Article.MARK_DRAFT
