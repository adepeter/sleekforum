from django.core.management import BaseCommand
from django.db.models import Count

from ...models import Thread


class Command(BaseCommand):
    help = 'Management command to manipulate users who view threads'

    # def add_arguments(self, parser):
    #     parser.add_argument('update', '-u', '--update', type=int, help='Update thread viewer for thread')

    def handle(self, *args, **options):
        for thread in Thread.objects.annotate(count_views=Count('thread_views')):
            thread.views = thread.count_views
            thread.save(update_fields=['views'])
            self.stdout.write(self.style.SUCCESS('%s was successfully updated' % thread.title))
