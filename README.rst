django-static-url - Generates dynamic static URL
================================================

:Authors:
  Resulto Developpement Web Inc.
:Version: 0.1.0

By default, the URI of static resources does not change between deployment and
it is up to each project to come with a solution to invalidate the browser's
cache. django-static-url adds helper functions that can be used in
Django settings file, in views and templates. The idea is to generate a new
/static/ URL each time the dev server is reloaded and a new URL each time the
code is deployed in production.

How does it work?
-----------------

In its simplest form, django-static-url will compute a hash based on the
current time and insert this hash between the static url prefix (e.g.,
/static/) and the static file path. The URL will be recomputed every time the
devserver is reloaded so any changes to static files should be picked up by the
browser without having to empty or bypass the cache.

In production, you probably do not want the URL to change every time a process
is reloaded so you can provide the path of a file whose access time will be
used to compute the hash. For example, we give the path of our uwsgi config
file because it is accessed only once per deployment.

More strategies will be provided in the future to accommodate various scenarios
(e.g., load balanced app servers that do not share files).

django-static-url assumes that you know how to configure your production web
server. Presumably, you are using nginx and have added a location block to
bypass the python web server to serve your static files. We provide an example
location block for nginx in the installation instructions below.

Requirements
------------

django-static-url works with Python 3.4+. It requires Django 1.8+

Installation
------------

Install the library
~~~~~~~~~~~~~~~~~~~

::

    pip install django-static-url


Add this snippet in your Django Settings (development)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    # The prefix of the static URL.
    STATIC_ROOT_URL = "/static/"

    # Will change the URL everytime the settings/server is reloaded.
    from django_static_url_helper import url_helper
    STATIC_URL = url_helper.get_static_url_now(
        STATIC_ROOT_URL, True, SECRET_KEY)


Alternative 2: Add this snippet in your Django Settings (production)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


::

    # The prefix of the static URL.
    STATIC_ROOT_URL = "/static/"

    # Will change the URL everything the SOME_IMPORTANT_FILE_PATH is touched
    # (url generated based on access time).
    from django_static_url_helper import url_helper
    STATIC_URL = url_helper.get_static_url_file(
        STATIC_ROOT_URL,
        SOME_IMPORTANT_FILE_PATH, True,
        SECRET_KEY)


Add this to your urls file (development)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    from django.conf import settings
    from django_static_url_helper.django_url_helper import staticfiles_dynamicurlpatterns

    # Define your urlpatterns here
    urlpatterns = ...

    if settings.DEBUG:
        urlpatterns += staticfiles_dynamicurlpatterns(settings.STATIC_ROOT_URL)


Add this to your nginx config file (production)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    # regex that captures all requests made to
    # /static(/HASH_CODE)/STATIC_FILE_PATH

    location ~ ^/static/([a-f0-9-]+/)?(.*)$ {
        # Set static file expiration
        expires 7d;
        alias /path/to/djangoproject/static/$2;
    }


License
-------

This software is licensed under the `New BSD License`. See the `LICENSE` file
in the repository for the full license text.


Signing GPG Key
---------------

The following GPG keys can be used to sign tags and release files:

- Barthelemy Dagenais: 76320A1B901510C4
