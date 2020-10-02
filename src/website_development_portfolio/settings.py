"""
Shared settings
"""

import os
import environ

project_root = environ.Path(__file__) - 4
env = environ.Env()
environ.Env.read_env()

# Main folder for source code
BASE_DIR = project_root()

# DEBUG is default to `True` meaning development server
DEBUG = env.bool('DEBUG', default=True)

if DEBUG:
    SECRET_KEY = env.str(
        'SECRET_KEY', default='(758q2z2l+47@s4ffq+2t@wqvr*@zoi1^7r8+_fh^9)&3v2cnz')
    ALLOWED_HOSTS = []
elif not DEBUG:
    from website_development_portfolio.settings.production import PRODUCTION_HOSTS
    SECRET_KEY = os.environ['SECRET_KEY']
    ALLOWED_HOSTS = PRODUCTION_HOSTS


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


database_root = project_root()


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'development.sqlite3'),
        }
    }
else:
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

public_root = project_root.path('public/')

# Virtual website path for static files
STATIC_URL = env.str('STATIC_URL', default='/static/')

# Physical server path for static files
STATIC_ROOT = public_root('staticfiles')

# Static files directory for project
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# Virtual website path for media files
MEDIA_URL = env.str('MEDIA_URL', default='/media/')

# Physical server path for media files
MEDIA_ROOT = public_root('media')

# Email Section
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_USE_TLS = True

EMAIL_PORT = 587

EMAIL_HOST_USER = ''

EMAIL_HOST_PASSWORD = ''
