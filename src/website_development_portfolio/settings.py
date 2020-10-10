""" Project Settings """

import dj_database_url
import os
from pathlib import Path
from decouple import config


BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


DEBUG = False


if DEBUG:
    SECRET_KEY = config('SECRET_KEY')
elif not DEBUG:
    SECRET_KEY = config('SECRET_KEY')


ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '.vercel.app'
    'lokotamathemastermind2website.herokuapp.com',
]


INSTALLED_APPS = [
    # Default applications
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Installed applications
    'main',
    'extra',
    'management',

    # 3rd party libraries
    'django_cleanup',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'website_development_portfolio.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'website_development_portfolio.wsgi.application'


if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'development.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DATABASE_NAME'),
            'USER': config('DATABASE_USER'),
            'PASSWORD': config('DATABASE_PASSWORD'),
            'HOST': config('DATABASE_HOST'),
            'PORT': config('DATABASE_PORT'),
        }
    }


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


LANGUAGE_CODE = 'en-us'


TIME_ZONE = 'UTC'


USE_I18N = True


USE_L10N = True


USE_TZ = True


STATIC_URL = '/static/'


PUBLIC_ROOT = os.path.join(BASE_DIR, 'public')


STATIC_ROOT = os.path.join(PUBLIC_ROOT, 'staticfiles')


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]


MEDIA_URL = '/media/'  # Website path for media files


MEDIA_ROOT = os.path.join(PUBLIC_ROOT, 'media')


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


EMAIL_HOST = 'smtp.gmail.com'


EMAIL_USE_TLS = True


EMAIL_PORT = 587


if DEBUG:
    EMAIL_HOST_USER = config('EMAIL_ID')
    EMAIL_HOST_PASSWORD = config('EMAIL_PASSWORD')
elif not DEBUG:
    EMAIL_HOST_USER = config('EMAIL_ID')
    EMAIL_HOST_PASSWORD = config('EMAIL_PASSWORD')


LOGIN_URL = '/admin/'


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


if not DEBUG:
    DATABASE_URL = config('DATABASE_URL')
    production_database = dj_database_url.config(
        default=DATABASE_URL, conn_max_age=500)
    DATABASES['default'].update(production_database)
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SESSION_EXPIRE_AT_BROWSER_CLOSE = True
