from ._devstage_bridge import *

INSTALLED_APPS += [
    'sleekapps.visits.apps.VisitsConfig',
]

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
