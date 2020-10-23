from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.templatetags.static import static
from django.utils.timezone import now

date_now = now()


def get_static(path_to_file_or_directory):
    if settings.DEBUG:
        return staticfiles_storage.url(path_to_file_or_directory)
    else:
        return static(path_to_file_or_directory)


def calculate_days_interval(date_obj):
    diff = date_now - date_obj
    return diff.days
