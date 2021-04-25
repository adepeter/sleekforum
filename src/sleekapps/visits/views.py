import datetime

from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.utils import timezone

from ..activity.models import Visit

User = get_user_model()


def visits(request, *args, **kwargs):
    user = User.objects.get(username='adepeter')
    today = datetime.datetime.today()
    visits = Visit.objects.filter(timestamp__date=today)
    # Visit.objects.create(user=user)
    qs = Visit.objects.visits_for_user_by(username=user.username)
    print(qs)
    return HttpResponse(f"""
    <h1>{today}\n\n{visits}\n\n{qs}</h1>
    """.format(today=today, visits=visits, qs=qs))
