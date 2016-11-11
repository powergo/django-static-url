from datetime import timedelta

import pytz

import django.utils.timezone


# Monkey patching necessities
# - make_aware

old_make_aware = django.utils.timezone.make_aware


def dst_make_aware(value, timezone=None, is_dst=None):
    """Calls make_aware but adds an extra hour if we encounter ambiguous time.

    reference: https://code.djangoproject.com/ticket/22598
    """
    try:
        return old_make_aware(value, timezone, is_dst)
    except (pytz.NonExistentTimeError, pytz.AmbiguousTimeError):
        # This will work for most cases in the northern hemisphere
        if value.hour <= 3:
            return old_make_aware(value + timedelta(hours=1))
        else:
            raise

django.utils.timezone.make_aware = dst_make_aware
