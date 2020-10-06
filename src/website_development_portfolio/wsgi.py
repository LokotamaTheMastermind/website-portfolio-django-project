""" WSGI """

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'website_development_portfolio.settings')

application = get_wsgi_application()

os.system('python manage.py makemigrations && python manage.py migrate')
os.system('python manage.py collectstatic')
os.system('python manage.py create_admin_user')
