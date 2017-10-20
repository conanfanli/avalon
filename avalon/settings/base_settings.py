"""
Django settings for avalon project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
import typing
import datetime
import os
from django.core.exceptions import ImproperlyConfigured

import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
ENV_VARS = {}
UNSET_ENV_VARS = {}


def get_environ(key, default=None, required=False):
    '''Return the value of the environment variable.

    Args:
        key (str): Name of the environment variable.
        default: Default value of the environment variable if not defined.
        required: Set to True to raise ImproperlyConfigured when the environment
    variable is not defined.
    '''
    if key not in os.environ and required and default is None:
        raise ImproperlyConfigured('Setting {} is required'.format(key))

    if key in os.environ:
        value = os.environ[key]
        ENV_VARS[key] = value
        return value
    else:
        UNSET_ENV_VARS[key] = default
        return default


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_environ('SECRET_KEY',
                         't@r9#f@r^hg4j#5%hfqgx&7vyxtsbzpf9a52zr6@=oq-t&(2_3')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS: typing.List = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'rest_framework',
    'corsheaders',

    'avalon.core',
]

MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # CORS
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'avalon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'avalon.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config(default='postgres://postgres:@localhost:5432/avalon')
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': get_environ('avalon_DB_NAME', 'avalon'),
#         'USER': get_environ('avalon_DB_USER', 'postgres'),
#         'PORT': get_environ('avalon_DB_PORT', ''),
#         'PASSWORD': get_environ('avalon_DB_PASSWORD', ''),
#         'HOST': get_environ('avalon_DB_HOST', ''),
#         'CONN_MAX_AGE': int(get_environ('avalon_CONN_MAX_AGE', 0)),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

ATOMIC_REQUESTS = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    # Default page size
    'PAGE_SIZE': 40,
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'avalon.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
    )
}


CORS_ORIGIN_REGEX_WHITELIST = ('^http://localhost',)
CORS_ALLOW_CREDENTIALS = True

LOGGING = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(levelname)s: %(name)s %(message)s'
        },
        # You may need to specify the timezone here.
        # For example: %(asctime)s CST [%(levelname)s] %(name)s:
        # %(message)s
        'standard': {
            'format': '[%(asctime)s %(levelname)s/%(process)d] [%(name)s]: %(message)s'
        },
    },

    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },

    'loggers': {
        '': {
            # Root handler
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
        'avalon': {
            'handlers': ['console'],
            'propagate': False,
        },
        'django': {
            'handlers': ['console'],
            'propagate': False,
        },
    }
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(minutes=60)
}
