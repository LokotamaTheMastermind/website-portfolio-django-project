from website_development_portfolio.settings.common import *
from decouple import config

DEBUG = True

SECRET_KEY = config(
    'SECRET_KEY', default='(758q2z2l+47@s4ffq+2t@wqvr*@zoi1^7r8+_fh^9)&3v2cnz')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'development.sqlite3',
    }
}

EMAIL_HOST_USER = config('EMAIL_USERNAME', default='')

EMAIL_HOST_PASSWORD = config('EMAIL_PASSWORD', default='')
