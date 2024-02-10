from django import template
from django.utils.timesince import timesince
from django.utils.timezone import now

register = template.Library()


@register.filter(name='time_since')
def time_since_filter(value):
    """
    Returns string representing "time since" e.g. "4 hours ago", "2 days ago".
    """
    if not value:
        return ''
    return timesince(value)
