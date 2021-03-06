"""
Django settings for txuwa-server-backend project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import raven

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEPLOYMENT = os.environ.get("DEPLOYMENT", "LOCAL")

# Frontend settings
if DEPLOYMENT == "PRODUCTION":
    FRONTEND_FOLDER_DIR = os.path.abspath(
        os.path.join(BASE_DIR, "../front-end/"))
else:
    FRONTEND_FOLDER_DIR = os.path.abspath(
        os.path.join(BASE_DIR, "../tedxuwa-react/"))

FRONTEND_TEMPLATE_DIR = os.path.join(FRONTEND_FOLDER_DIR, "build/")
FRONTEND_STATIC_DIR = os.path.join(BASE_DIR, "static/")
FRONTEND_STATIC_FILES = os.path.join(FRONTEND_STATIC_DIR, "static/")
FRONTEND_ENTRY_POINT = os.path.join(
    FRONTEND_STATIC_DIR, "index.html")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY",
                            "local1!a^f1*w-*q8i6g!kft@6-1sbc!av&tx+u_2uy0z18)jp5=vj$")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = DEPLOYMENT != "PRODUCTION"
# DEBUG = True
ALLOWED_HOSTS = [
    ".tedxuwa.com",
    "localhost",
]

# Application definition

INSTALLED_APPS = [
    # django stuff
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    # packages
    'raven.contrib.django.raven_compat',
    'corsheaders',
    'admincolors',
    'rest_framework',
    'sslserver',
    'constance.backends.database',
    'constance',
    # user written
    'main',
    'tedxuwa_user',
    'events',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'root.urls'

ADMIN_COLORS_BASE_THEME = 'TED Red'
ADMIN_COLORS = [
    ('Default', []),
    ('TED Red', 'admin_colours.css'),
    ('Lite', 'admincolors/css/lite.css'),
    ('Dark Blue', 'admincolors/css/dark-blue.css'),
    ('Gray', 'admincolors/css/gray.css')
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [FRONTEND_STATIC_DIR,
                 os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'admincolors.context_processors.admin_theme',
            ],
        },
    },
]

WSGI_APPLICATION = 'root.wsgi.application'

AUTH_USER_MODEL = 'tedxuwa_user.User'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# CORS
# https://github.com/ottoyiu/django-cors-headers
CORS_ORIGIN_WHITELIST = (
    'google.com',
    'tedxuwa.com',
    'www.tedxuwa.com',
    'localhost:8000',
    'localhost:3000',
    '127.0.0.1:8000',
    '127.0.0.1:3000',
)
# just disable it
CORS_ORIGIN_ALLOW_ALL = True


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Australia/Perth'  # TEDxUWA is based in Perth, duh...

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, "static"))
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# set 1 year browser cache
WHITENOISE_MAX_AGE = 31536000

STATICFILES_DIRS = (
    FRONTEND_TEMPLATE_DIR,
    FRONTEND_STATIC_FILES,
    "root/common_static/"  # general static files
)


# REST framework settings
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 50
}


RATELIMIT_ENABLE = True


# Sentry configs
# https://sentry.io/tedxuwa/tedxuwa/getting-started/python-django/
# only allow on production
if DEPLOYMENT == "PRODUCTION":
    RAVEN_CONFIG = {
        'dsn': 'https://4a10c69575b9428da91136badfd541e9:89104fdd40a2426abbdc35a049dd5a24@sentry.io/1190737',
        # If you are using git, you can also automatically configure the
        # release based on the git info.
        # https://github.com/getsentry/raven-python/issues/855
        'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
    }
    PAPERTRAIL_LOG_DESTINATION = os.environ.get("PAPERTRAIL_LOG_DESTINATION",
                                                "dummypapertraillink")
    # intergrate with logging to send errors to sentry automatically
    # https://docs.sentry.io/clients/python/integrations/django/#integration-with-logging
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': DEPLOYMENT == "PRODUCTION",
        'root': {
            'level': 'ERROR',
            'handlers': ['sentry', 'papertrail'],
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s %(asctime)s %(module)s '
                '%(process)d %(thread)d %(message)s'
            },
        },
        'handlers': {
            'sentry': {
                # To capture more than ERROR, change to WARNING, INFO, etc.
                'level': 'ERROR',
                'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
                'tags': {'custom-tag': 'x'},
            },
            'papertrail': {
                'level': 'DEBUG',
                'class': 'logging.handlers.SysLogHandler',
                'address': PAPERTRAIL_LOG_DESTINATION
            },
            'console': {
                'level': 'ERROR',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            },
            'null': {
                'level': 'DEBUG',
                'class': 'logging.NullHandler',
            },
        },
        'loggers': {
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': ['console'],
                'propagate': False,
            },
            'raven': {
                'level': 'ERROR',
                'handlers': ['console'],
                'propagate': False,
            },
            'sentry.errors': {
                'level': 'ERROR',
                'handlers': ['console'],
                'propagate': False,
            },
            'papertrail': {
                'level': 'INFO',
                'handlers': ['console', 'papertrail'],
                'propagate': True,
            },
            'django.security.DisallowedHost': {
                'handlers': ['null'],
                'propagate': False,
            },
        },
    }

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_CONFIG = {
    'TICKET_FORWARD_LINK': ('https://tedxuwa.com', 'where to forward tickets.tedxuwa.com to'),
    'REACH_FOLLOWERS': ('3k', 'number of followers'),
    'REACH_SPEAKERS': ('80', 'number of speakers'),
    'REACH_SUBSCRIBERS': ('854', 'number of subscribers')
}
