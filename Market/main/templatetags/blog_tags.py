from django import template

from django.template.defaultfilters import stringfilter

from django.contrib.auth.models import User

import datetime
from django.utils.timezone import utc

register = template.Library()


@register.simple_tag
def current_time():
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    return now


@register.filter
@stringfilter
def palindrome(string):
    reversed_string = string[::-1]
    return  reversed_string
