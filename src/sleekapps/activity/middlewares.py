import datetime

from django.core.cache import cache


class LastVisitUpdaterMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        today = datetime.datetime.today()
        current_user = request.user
        last_login_cache = None
        if current_user.is_authenticated:
            last_login_cache = cache.get('%s_last_visit_date' % current_user.username)
        response = self.get_response(request)
        if last_login_cache is None and current_user.is_authenticated:
            cache.set(
                '%s_last_visit_date' % current_user.username,
                today,
                timeout=60*60*24
            )
            current_user.user_visits.create()
        return response

