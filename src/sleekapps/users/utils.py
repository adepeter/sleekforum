from django.contrib.contenttypes.models import ContentType

from django.utils import timezone


class ImageHandler:

    def upload_to(self, instance, filename):
        random_int = timezone.now() - instance.created
        filename = str(random_int.microseconds) + '_' + filename
        instance_content_type = ContentType.objects.get_for_model(instance)
        app_name = instance_content_type.app_label
        instance_model = instance_content_type.model
        return f'{app_name}/{instance_model}/{filename}'

    def get_dp_or_first_char(self, avatar):
        user_ct = ContentType.objects.get_for_model(avatar)
        return user_ct.username
