from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class GraphQLConfig(AppConfig):
    name = 'sleekapps.graphql'
    models_module = None
    label = 'graphql'
    verbose_name = _('GraphQL')