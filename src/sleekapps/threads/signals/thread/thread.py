from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal

from .models import Thread, ThreadView

# from ..miscs.models.activity import Action
# from ..miscs.signals.activity import activity_updater


# #
# # @receiver(post_save, sender=Action)
# # def like_and_dislike_handler(sender, instance, created, **kwargs):
# #     from django.contrib.contenttypes.models import ContentType
# #     ct = ContentType.objects.get_for_model(instance).get_object_for_this_type()
# #     if created:
# #         get_ct_for_obj_of_instance = instance.content_object
# #         if instance.action_value == Action.LIKE:
# #             get_ct_for_obj_of_instance.likes = ct
# #             print('Ading likes counter')
# #         else:
# #             print('Adding dislike counter')
# #             get_ct_for_obj_of_instance.dislikes = ct
# #         get_ct_for_obj_of_instance.save()
# #
# #
# # # @receiver(activity_updater)
# # # def hal(sender, **kwargs):
# # #     print('Sender is', sender, kwargs.get('obj'))
