from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from ...models import Thread

from ...viewmixins.thread import ThreadSingleActionMiscView


class LockUnlockThread(ThreadSingleActionMiscView):
    model = Thread
    boolean_field = 'is_locked'
    redirect_to_threads = False

    def get(self, request, *args, **kwargs):
        self.success_message()
        return super().get(request, *args, **kwargs)

    def success_message(self):
        obj = self.get_object()
        if not obj.is_locked:
            msg = _(f'{obj.title} was locked successfully')
        else:
            msg = _(f'{obj.title} was successfully unlocked')
        messages.success(self.request, msg)
