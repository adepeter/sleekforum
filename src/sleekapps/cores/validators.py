from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_image_filesize(file):
    if file.size > 1024 * 1024:
        raise ValidationError(
            _('Exceeded image maximum file size of 1MB'),
            code='category_image_too_large'
        )
