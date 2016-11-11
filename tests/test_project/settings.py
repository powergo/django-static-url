import os
import sys

# Import source code dir
#   This ensures that we can import `resulto_dj.xyz...` from within the tests/
#   folder containing all the tests from the lib code.
sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.join(os.getcwd(), os.pardir))
sys.path.insert(0, os.path.join(os.getcwd(), os.pardir, os.pardir))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = "abcdef123-"

DEBUG = True
IN_TEST = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        # XXX This assumes you have the loyalty project setup on your machine
        # for running tests. Postgres engine is necessary because of the usage
        # of Postgres' JSONField in the tests and the library and there must
        # be an existing Postgres DB from your machine in these settings.
        "NAME": "loyalty",
        "USER": "loyalty",
        "PASSWORD": "loyalty",
        "PORT": 5432,
        "HOST": "127.0.0.1",
    }
}

MIDDLEWARE_CLASSES = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    'django.contrib.messages.middleware.MessageMiddleware',
)


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    'django.contrib.messages',
    "django.contrib.staticfiles",
    "django_jinja",
    "django_jinja.contrib._humanize",
    "django_makemessages_xgettext",
    "daterange_filter",
    "tests.test_app"
]

PASSWORD_HASHERS = (
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.BCryptPasswordHasher",
)

TEMPLATES = [
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        "APP_DIRS": True,
        "OPTIONS": {
            "match_extension": ".j2",
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
            "globals": {
                "get_current_date": "resulto_dj.jinja_lib.get_current_date",
            }
        }
    },
    {
        "BACKEND":
            "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        }
    },
]

DEFAULT_JINJA2_TEMPLATE_EXTENSION = ".j2"


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(message)s"
        },
        "simple": {
            "format": "%(levelname)s %(message)s"
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple"
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.request": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": False,
        },
        "celery": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "resulto_dj": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        }
    },
}


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

TIME_ZONE = "America/Montreal"

USE_I18N = True

USE_L10N = True

USE_THOUSAND_SEPARATOR = True

USE_TZ = True

SITE_ID = 1

OVERRIDE_CURRENT_IP = None


# LANGUAGES
LANGUAGE_CODE = "en"


ugettext = lambda s: s  # dummy ugettext function, as django"s docs say


LANGUAGES = (
    ("en", ugettext("English")),
    ("fr", ugettext("French")),
)

ADMINS = (
    ("Dev Team", "dev@resulto.ca"),
)

STATIC_URL = "/static/"

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
)

STATIC_ROOT = os.path.join(BASE_DIR, "static")


try:
    if os.environ.get("CIRCLECI") == "true":
        current_module = sys.modules[__name__]
        from tests.test_project.circleci_settings import configure
        configure(current_module)
except ImportError:
    pass
