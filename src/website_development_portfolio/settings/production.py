from website_development_portfolio.settings.common import *
import os

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = [
    '.vercel.app',
    '127.0.0.1',
    'localhost'
]

EMAIL_HOST_USER = os.environ['EMAIL_USERNAME']

EMAIL_HOST_PASSWORD = os.environ['EMAIL_PASSWORD']
