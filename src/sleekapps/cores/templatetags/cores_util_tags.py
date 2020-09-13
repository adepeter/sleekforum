import math

# from precise_bbcode.bbcode import get_parser
from django import template
from django.template.defaultfilters import stringfilter
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.translation import ngettext, gettext_lazy as _

from ..helper import calculate_days_interval

register = template.Library()
# parser = get_parser()


@register.filter
@stringfilter
def first_char(chars):
    return chars[0].lower()


@register.filter(expects_localtime=True)
def time_ago(param):
    now = timezone.now()
    diff = now - param
    currently = _('just now')
    if diff.days == 0 and 30 < diff.seconds < 60:
        currently = _('%s seconds ago') % diff.seconds
    elif diff.days == 0 and 60 <= diff.seconds < 3600:
        minutes = math.floor(diff.seconds / 60)
        currently = ngettext(_('%(minutes)d minute ago'),
                             _('%(minutes)d minutes ago'), minutes) % {
                        'minutes': minutes
                    }
    elif diff.days == 0 and 3600 <= diff.seconds < 86400:
        hours = math.floor(diff.seconds / 3600)
        currently = ngettext(_('%(hours)d hour ago'),
                             _('%(hours)d hours ago'), hours) % {
                        'hours': hours
                    }
    elif 1 <= diff.days <= 7:
        days = diff.days
        currently = ngettext(_('%(days)d day ago'),
                             _('%(days)d days ago'), days) % {
                        'days': days
                    }
    elif 7 <= diff.days <= 30:
        weeks = math.floor(diff.days / 7)
        currently = ngettext(_('%(weeks)d week ago'),
                             _('%(weeks)d weeks ago'), weeks) % {
                        'weeks': weeks
                    }
    elif 30 <= diff.days <= 365:
        months = math.floor(diff.days / 30)
        currently = ngettext(_('%(months)d month ago'),
                             _('%(months)d months ago'), months) % {
                        'months': months
                    }
    elif diff.days >= 365:
        years = math.floor(diff.days / 365)
        currently = ngettext(_('%(years)d year ago'),
                             _('%(years)d years ago'), years) % {
                        'years': years
                    }
    return currently


@register.filter
def pretty_count(value, decimal_place=1):
    if isinstance(value, int):
        views = str(value)
        if 3 <= len(views) <= 6:
            views = round(int(views) / 1000, decimal_place)
            result = '%(views)sk' % {'views': views}
        elif 6 <= len(views) <= 9:
            views = round(int(views) / 1000000, decimal_place)
            result = '%(views)sM' % {'views': views}
        else:
            result = views
        return result


@register.filter
def unit_to_tens(value):
    "Convert pagination in unit digit to tens."
    value = str(value)
    if len(value) < 2:
        value = '0' + value
    return value


@register.filter
def get_dictionary_value(result, key):
    try:
        return result[key]
    except KeyError:
        return None


@register.simple_tag(name='days_past_interval')
def interval_calculator(date_obj):
    return calculate_days_interval(date_obj)

@register.filter(need_autoescape=False, is_safe=True)
@stringfilter
def dont_escape(text):
    return mark_safe(text)
    # return mark_safe(parser.render(text))
