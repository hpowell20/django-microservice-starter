"""
WSGI config for serviceproject project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service.settings")

application = get_wsgi_application()