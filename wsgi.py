"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from json import load

from django.core.wsgi import get_wsgi_application

ENVIRNMENT = load(open('secret_sauce.json','r'))["APP_ENV"]
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{ENVIRNMENT}')

application = get_wsgi_application()
