"""
WSGI config for IN350M4_LeoanrdWalker project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IN350M4_LeoanrdWalker.settings')

application = get_wsgi_application()
