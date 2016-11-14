from django.conf.urls import url
from django.contrib.staticfiles.views import serve


def staticfiles_dynamicurlpatterns(static_url="/static/"):
    """Returns url patterns that can resolve dynamic static URL.
    """
    return [
        url(r'^{0}(?:/[a-f0-9-]+)?/(?P<path>.*)$'
            .format(static_url[1:-1]),
            serve),
    ]
