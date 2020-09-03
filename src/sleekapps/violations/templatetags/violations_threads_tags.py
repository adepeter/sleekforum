from django import template
from django.db.models import Avg, Sum, Count
from violation.models import Violation

register = template.Library()


@register.simple_tag
def violations_in_thread(thread):
    posts = thread.posts.all()
    violations_by_thread = thread.violations.all().count()
    violations_by_posts = Violation.objects.filter(posts__in=posts).count()
    total_violations_in_thread = sum([violations_by_thread, violations_by_posts])
    aggregated_violations = Violation.objects.aggregate(
        count_thread=Count('threads'),
        count_posts=Count('posts')
    )
    total = aggregated_violations['count_thread'] + aggregated_violations['count_posts']
    percentile = round(total_violations_in_thread / total * 100, 1)
    return dict(
        (('percentile', percentile), ('violations_in_thread', total_violations_in_thread))
    )
