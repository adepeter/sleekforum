from django.db.models import F
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver, Signal

from ...models import Thread, ThreadView

thread_views_creator_and_updater = Signal()


@receiver(post_save, sender=Thread)
def thread_view_creator(sender, instance, created, **kwargs):
    if created:
        instance.thread_views.create(user=instance.starter, views=1)
    views_count = instance.thread_views.count()
    Thread.objects.filter(id=instance.id).update(views=views_count)


@receiver(thread_views_creator_and_updater)
def handle_thread_views(sender, **kwargs):
    request, thread = kwargs['request'], kwargs['thread']
    if request.user.is_authenticated:
        viewer = ThreadView.objects.filter(user=request.user, thread=thread)
        if viewer.exists():
            viewer.update(views=F('views') + 1)
        else:
            ThreadView.objects.create(user=request.user, thread=thread, views=1)
    thread.views = thread.thread_views.count()
    thread.save(update_fields=['views'])


@receiver(post_delete, sender=ThreadView)
def update_deleted_thread_viewers(sender, instance, using, **kwargs):
    instance.thread.views = instance.thread.thread_views.count()
    instance.thread.save(update_fields=['views'])


__all__ = [
    'thread_view_creator',
    'handle_thread_views',
    'thread_views_creator_and_updater',
    'update_deleted_thread_viewers'
]
