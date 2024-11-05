"""Django settings for example_project project."""
import os

import portal
import environ
DEBUG = True
env = environ.Env(
    DEBUG=(bool, False)
)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
ROOT_URLCONF = 'example_project.urls'
WSGI_APPLICATION = 'example_project.wsgi.application'
api_url = env('BASE_URL')+'/studio/artifacts/artifact/update/'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": DEBUG,
            "context_processors": [
                "django.template.context_processors.request",
                "django.template.context_processors.debug",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "sekizai.context_processors.sekizai",
            ],
        },
    }
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        "NAME": os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "db.sqlite3"
        ),  # Or path to database file if using sqlite3.
        "ATOMIC_REQUESTS": True,
    }
}
class DisableMigrations:
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None

# MIGRATION_MODULES = DisableMigrations()
# DATABASES = {
#     'default': {
#         'ENGINE': env('DATABASE_ENGINE'),  # e.g., 'django.db.backends.postgresql'
#         'NAME': 'steamhubdb_1',
#         'USER': 'osamashoman',
#         'PASSWORD': 'admin12345',
#         'HOST': 'steamhub-1.cqgixiadbngn.us-east-1.rds.amazonaws.com',
#         'PORT': env('DATABASE_PORT'),
#     }
# }


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

USE_I18N = True
USE_L10N = True
USE_TZ = True

TIME_ZONE = "Europe/London"
LANGUAGE_CODE = "en-gb"
LANGUAGES = (("en-gb", "English"), ("lol-us", "Localisation"))

LOCALE_PATHS = [
    # This shouldn't be needed, but it looks like there's an issue with
    # using a language code that's not in `django/conf/locale` - the
    # check_for_language function doesn't recognise it.
    os.path.join(os.path.dirname(__file__), "locale")
]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "./game/static/"),

    os.path.join(os.path.dirname(portal.__file__), "static"),  # Portal package static files
]

SECRET_KEY = "m%nv-45ld@&6ui+!xumd954f9!yyz2-_a^*ys4v6o@pnnb--$8"


INSTALLED_APPS = (
    "game",
    "pipeline",
    "portal",
    "common",
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_reverse_js",
    "django_otp",
    "django_otp.plugins.otp_static",
    "django_otp.plugins.otp_totp",
    "rest_framework",
    "import_export",
    "sekizai",  # for javascript and css management
)

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

ALLOWED_HOSTS = ["*"]
PIPELINE_ENABLED = False

PIPELINE = {
    "SASS_ARGUMENTS": "--quiet",
    "COMPILERS": ("game.pipeline_compilers.LibSassCompiler",),
    "STYLESHEETS": {
        "css": {
            "source_filenames": (
                "portal/sass/bootstrap.scss",  # Make paths relative
                "portal/sass/colorbox.scss",
                "portal/sass/styles.scss",
            ),
            "output_filename": "portal/portal.css",
        },
        "popup": {
            "source_filenames": ("portal/sass/partials/_popup.scss",),  # Make paths relative
            "output_filename": "portal/popup.css",
        },
        "game-scss": {
            "source_filenames": ("game/sass/game.scss",),  # Make paths relative
            "output_filename": "game.css",
        },
    },
    "CSS_COMPRESSOR": None,
}


STATICFILES_FINDERS = [
    "pipeline.finders.PipelineFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# This is used in common to enable/disable the OneTrust cookie management script
COOKIE_MANAGEMENT_ENABLED = False

CLOUD_STORAGE_PREFIX = "https://storage.googleapis.com/codeforlife-assets/"
SITE_ID = 1

try:
    from example_project.local_settings import *  # pylint: disable=E0611
except ImportError:
    pass

from common.csp_config import *
