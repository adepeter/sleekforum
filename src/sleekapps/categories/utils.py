import os
import uuid
from PIL import Image
from django.contrib.contenttypes.models import ContentType


def resize_image(avatar, size=(64, 64)):
    image = Image.open(avatar.path)
    image.resize(size, Image.ANTIALIAS).save(avatar.path, 'PNG', quality=100)


def handle_uploaded_image(instance, filename):
    uuid4 = str(uuid.uuid4())
    base, ext = os.path.splitext(filename)
    new_filename = ''.join(uuid4.split('-'))
    filename = new_filename + ext.lower()
    instance_content_type = ContentType.objects.get_for_model(instance)
    app_name = instance_content_type.app_label
    return f'{app_name}/{filename}'
