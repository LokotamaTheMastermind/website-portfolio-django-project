""" Project Settings """

import os
from pathlib import Path
from decouple import config


BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


DEBUG = True


if DEBUG:
    SECRET_KEY = config('SECRET_KEY')
elif not DEBUG:
    SECRET_KEY = os.environ['SECRET_KEY']


ALLOWED_HOSTS = []


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


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'development.sqlite3',
        }
    }
elif not DEBUG:
    DATABASE = {}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# Virtual website path for static files
STATIC_URL = '/static/'

PUBLIC_ROOT = os.path.join(BASE_DIR, 'public')

# Physical server path for static files
STATIC_ROOT = os.path.join(PUBLIC_ROOT, 'staticfiles')

# Static files directory for project
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# Virtual website path for media files
MEDIA_URL = '/media/'

# Physical server path for media files
MEDIA_ROOT = os.path.join(PUBLIC_ROOT, 'media')

# Email Section
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_USE_TLS = True

EMAIL_PORT = 587

if DEBUG:
    EMAIL_HOST_USER = config('EMAIL_ID')
    EMAIL_HOST_PASSWORD = config('EMAIL_PASSWORD')
elif not DEBUG:
    EMAIL_HOST_USER = os.environ['EMAIL_ID']
    EMAIL_HOST_PASSWORD = os.environ['EMAIL_PASSWORD']

LOGIN_URL = '/admin/'
