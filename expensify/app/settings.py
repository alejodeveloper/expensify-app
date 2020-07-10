"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@50!2pbw1qs8zls$cb+zn61001amsuza_8b4abb65ti#h37_bp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get(
            'DB_ENGINE', 'django.db.backends.postgresql_psycopg2'
        ),
        'NAME': os.environ.get('DB_NAME', 'expensify-app'),
        'USER': os.environ.get('DB_USERNAME', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'expensify1234'),
        'HOST': os.environ.get('DB_HOST', 'postgresql-expensify-app'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

################################################################################
############################# CELERY SETTINGS  #################################
################################################################################
if os.environ.get('CELERY', False):
    remove_apps = [
        'django.contrib.sessions',
        'django.contrib.staticfiles',
        'rest_framework',
    ]
    for aplication in remove_apps:
        INSTALLED_APPS.remove(aplication)

REDIS_HOST = os.environ.get('REDIS_HOST', 'redis-expensify')
REDIS_PORT = os.environ.get('REDIS_PORT', '6379')

RABBIT_USER = os.environ.get('RABBITMQ_DEFAULT_USER', 'admin')
RABBIT_PSSWD = os.environ.get('RABBITMQ_DEFAULT_PASS', 'mypass')
RABBIT_HOST = os.environ.get('RABBITMQ_DEFAULT_HOST', 'rabbit-expensify')
RABBIT_PORT = os.environ.get('RABBITMQ_DEFAULT_PORT', '5672')

CELERY_BROKER_URL = f'amqp://{RABBIT_USER}:{RABBIT_PSSWD}@{RABBIT_HOST}:{RABBIT_PORT}'
CELERY_RESULT_BACKEND = None
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'America/Bogota'
