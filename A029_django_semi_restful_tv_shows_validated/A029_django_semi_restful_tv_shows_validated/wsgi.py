"""
WSGI config for A029_django_semi_restful_tv_shows_validated project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'A029_django_semi_restful_tv_shows_validated.settings')

application = get_wsgi_application()
