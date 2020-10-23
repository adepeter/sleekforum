from ...models import Thread
from ...viewmixins.thread import ThreadSingleActionMiscView


class HideUnhideThread(ThreadSingleActionMiscView):
    model = Thread
    boolean_field = 'is_hidden'
    redirect_to_threads = False
