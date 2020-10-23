from django.core.cache import cache
from django.db import models

from .managers import ConfigurationManager


class Configuration(models.Model):
    objects = ConfigurationManager()

    class Meta:
        abstract = True

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)

    def delete(self, *args, **kwargs):
        """Prevent object deletion"""

    def save(self, *args, **kwargs):
        if self.title is None:
            self.title = 'Sleekforum'
        self.id = 1
        super().save(*args, **kwargs)

    def set_cache(self):
        cache.set(self.__class__.__name__, self)

    def __str__(self):
        return 'Site configuration menu'
