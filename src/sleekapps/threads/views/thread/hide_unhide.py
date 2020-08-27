from ...models import Thread

from .thread_misc import ThreadSingleActionMiscView


class HideUnhideThread(ThreadSingleActionMiscView):
    model = Thread
    boolean_field = 'is_hidden'
    redirect_to_threads = False
