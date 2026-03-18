"""
ASGI config for IN350M4_LeoanrdWalker project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IN350M4_LeoanrdWalker.settings')

application = get_asgi_application()
