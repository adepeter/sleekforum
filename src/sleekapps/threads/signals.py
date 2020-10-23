from django.core.cache import cache
from django.db.models import F
from django.dispatch import receiver, Signal
from django.db.models.signals import post_save

from violation.signals import report_handler

# from ..miscs.models.activity import Action
# from ..miscs.signals.activity import activity_updater

from .models import Thread

thread_views_creator_and_updater = Signal(providing_args=['request', 'thread'])

@receiver(post_save, sender=Thread)
def handle_thread_view_creation(sender, instance, created, **kwargs):
    if created:
        thread_view_key = [('thread_%d', [instance.starter] % instance.id)]
        cache.set('thread_views', dict(thread_view_key), timeout=None)


@receiver(thread_views_creator_and_updater)
def handle_thread_views(sender, **kwargs):
    request, thread = kwargs['request'], kwargs['thread']
    if request.user.is_authenticated:
        thread_views_cache = cache.get('thread_views')
        thread_views_cache_key = 'thread_%d' % thread.id
        if thread_views_cache is not None:
            viewers = thread_views_cache.get(thread_views_cache_key)
            if request.user not in viewers:
                viewers.append(request.user)
                new_viewers = [(thread_views_cache_key, viewers)]
                cache.set('thread_views', dict(new_viewers), timeout=None)
        else:
            thread_view_key = [(thread_views_cache_key, [request.user])]
            cache.set('thread_views', dict(thread_view_key), timeout=None)



#
# @receiver(post_save, sender=Action)
# def like_and_dislike_handler(sender, instance, created, **kwargs):
#     from django.contrib.contenttypes.models import ContentType
#     ct = ContentType.objects.get_for_model(instance).get_object_for_this_type()
#     if created:
#         get_ct_for_obj_of_instance = instance.content_object
#         if instance.action_value == Action.LIKE:
#             get_ct_for_obj_of_instance.likes = ct
#             print('Ading likes counter')
#         else:
#             print('Adding dislike counter')
#             get_ct_for_obj_of_instance.dislikes = ct
#         get_ct_for_obj_of_instance.save()
#
#
# # @receiver(activity_updater)
# # def hal(sender, **kwargs):
# #     print('Sender is', sender, kwargs.get('obj'))
