from django.db import models


class VisitManager(models.Manager):
    def visits_for_user_by(self, **kwargs):
        fields = {}
        for field, value in kwargs.items():
            fields.update({'user__%s' % field: value})
        return self.filter(**fields)
