from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Category
from .utils import resize_image


@receiver(post_save, sender=Category)
def resize_category_image(sender, instance, created, **kwargs):
    if created:
        try:
            resize_image(instance.image)
        except Exception:
            pass
