import datetime

from django.core.cache import cache


class LastVisitUpdaterMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        today = datetime.datetime.today()
        current_user = request.user
        if current_user.is_authenticated:
            cache.set(
                '%s_last_visit_date' % current_user.username,
                today, timeout=60*60*24
            )
        response = self.get_response(request)
        if cache.get('%s_last_visit_date' % current_user.username) is None:
            current_user.user_visits.create()
        return response

