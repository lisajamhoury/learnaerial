"""
Django settings for learnaerial project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_WEBFACTION_DIR = os.path.dirname(os.path.dirname(BASE_DIR))


try:
    from learnaerial.environment import ENVIRONMENT
except ImportError:
    ENVIRONMENT = 'production'

try:
    from learnaerial.db_settings import DB_PASSWORD
except ImportError:
    DB_PASSWORD = ''

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=sf$s-&@ayl2(3&rfro=ywy#0w3jvvi$e%!oh+=2@0n5x)qug='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

if ENVIRONMENT == 'develop':
    DEBUG = True


ALLOWED_HOSTS = ['learnaerial.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_summernote',
    'imagekit',
    'main',
    'events',
    'listings',
    'blog',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # insert your TEMPLATE_DIRS here
            BASE_DIR + '/templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'main.context_processors.get_current_path',
            ],
        },
    },
]

ROOT_URLCONF = 'learnaerial.urls'

WSGI_APPLICATION = 'learnaerial.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default':{
       'NAME': 'learnaerial',
       'USER': 'learnaerial',
       'PASSWORD': DB_PASSWORD,
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
    }
}


if ENVIRONMENT == 'develop':
    DATABASES = {
        'default': {
           'NAME': 'learnaerial',
           'ENGINE': 'django.db.backends.postgresql_psycopg2',
       }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

STATICFILES_DIRS = (
    BASE_DIR + '/assets',
)

MEDIA_ROOT = BASE_WEBFACTION_DIR + '/learnaerial_media'
STATIC_ROOT = BASE_WEBFACTION_DIR + '/learnaerial_static'

if ENVIRONMENT == 'develop':
    MEDIA_ROOT = BASE_DIR + '/learnaerial_media'
    STATIC_ROOT = BASE_DIR + '/learnaerial_static'


MAILCHIMP_API_KEY = '3477524f7215966259c95cd4b96bb3eb-us4'

FACEBOOK_APP_ID = '377919919067435'
FACEBOOK_APP_SECRET = '1292e06dd33d3ddc2a5e6ef32b105ee2'
FACEBOOK_PAGE_ID = '839473479460641'
FACEBOOK_PAGE_TOKEN = 'CAAFXt1aHkSsBABXWIBE7BzJCLoFZBhsJJqSOZAcTPFz5UjPGOZC7QJWN4z8GyD8Tu9ZCJxlZAg8yHdYdxoU2Pe0eQA7PzPW0MW54mfXZBykhoqKfMd89A8ZBovfQU7IVozDgJT37ZA69ZBmznZA2QrO2upwjJYCkCVUJOSJkwJW0Vht177zgRpARvc'

SITE_DOMAIN = 'learnaerial.com'
SITE_URL = 'http://%s' % SITE_DOMAIN
