from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.templatetags.static import static

def get_static(path_to_file_or_directory):
    if settings.DEBUG:
        return staticfiles_storage.url(path_to_file_or_directory)
    else:
        return static(path_to_file_or_directory)