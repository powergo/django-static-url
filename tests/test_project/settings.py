import os
import sys

# Import source code dir
#   This ensures that we can import `django_static_url.xyz...` from within the tests/
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
        "NAME": "test",
        "USER": "test",
        "PASSWORD": "test",
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
