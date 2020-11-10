from django.apps import AppConfig

from django.utils.translation import gettext_lazy as _


class GraphQLConfig(AppConfig):
    name = 'sleekapps.graphql'
    label = 'sleekapps_graphql'
    verbose_name = _('Sleekforum GraphQL')
    models_module = None
