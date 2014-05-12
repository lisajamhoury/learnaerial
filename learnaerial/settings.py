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

try:
    from learnaerial.environment import ENVIRONMENT
except ImportError:
    ENVIRONMENT='production'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=sf$s-&@ayl2(3&rfro=ywy#0w3jvvi$e%!oh+=2@0n5x)qug='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

if ENVIRONMENT == 'develop':
    DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['learnaerial.com']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'main',
    'events',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'learnaerial.urls'

WSGI_APPLICATION = 'learnaerial.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default':{
       'NAME':'learnaerial',
       'USER': 'learnaerial',
       'PASSWORD': 'fop32fjpo2!!@222',
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
    }
}


if ENVIRONMENT == 'develop':
    DATABASES = {
        'default':{
           'NAME':'learnaerial',
           'ENGINE': 'django.db.backends.postgresql_psycopg2',
       }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    BASE_DIR + '/templates',
)

STATICFILES_DIRS = (
    BASE_DIR + '/assets',
)

MEDIA_ROOT = BASE_DIR + '/media'