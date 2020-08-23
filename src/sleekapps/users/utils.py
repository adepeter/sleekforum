from django.contrib.contenttypes.models import ContentType
from django.utils import timezone


class ImageHandler:

    def upload_to(self, instance, filename):
        random_int = timezone.now() - instance.date_created
        filename = str(random_int.microseconds) + '_' + filename
        instance_content_type = ContentType.objects.get_for_model(instance)
        app_name = instance_content_type.app_label
        instance_model = instance_content_type.model
        return f'{app_name}/{instance_model}/{instance.username}/{filename}'

    @staticmethod
    def get_avatar(user_obj):
        try:
            avatar = user_obj.avatar.url
        except ValueError:
            if user_obj.sex == 'male':
                avatar = '/default/users/avatars/male.jpg'
            elif user_obj.sex == 'female':
                avatar = '/defaults/users/avatars/female.jpg'
            else:
                avatar = '/defaults/users/avatars/none.jpg'
        return avatar