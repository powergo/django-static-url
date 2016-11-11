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

    # Will change the URL everytime the settings/server is reloaded.

    from django_static_url_helper import url_helper
    STATIC_URL = url_helper.get_static_url_now(
        STATIC_ROOT_URL, True, SECRET_KEY)


Alternative 2: Add this snippet in your Django Settings (production)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


::

    # Will change the URL everything the SOME_IMPORTANT_FILE_PATH is touched
    # (url generated based on access time).

    from django_static_url_helper import url_helper
    settings.STATIC_URL = url_helper.get_static_url_file(
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

    urlpatterns += staticfiles_dynamicurlpatterns(settings.STATIC_ROOT_URL)


Add this to your nginx config file (production)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    # regex that capture all requests made to
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

- Resulto Development Team: AEC378AB578FF0FC
- Barthelemy Dagenais: 76320A1B901510C4
