"""
WSGI config for asdjadhajs_dev_136664 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "asdjadhajs_dev_136664.settings"
)

application = get_wsgi_application()
