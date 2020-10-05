""" WSGI """

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'website_development_portfolio.settings')

application = get_wsgi_application()
