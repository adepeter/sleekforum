from django.db import models


class ConfigurationManager(models.Manager):
    def get(self, *args, **kwargs):
        return super().get(id=1)
