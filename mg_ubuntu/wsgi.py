"""
WSGI config for mg_ubuntu project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application
import os
import sys


sys.path.append('/home/mgutekunst/django_projects/mg_ubuntu/mg_ubuntu')
sys.path.append('/home/mgutekunst/django_projects/mg_ubuntu')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mg_ubuntu.settings')

application = get_wsgi_application()
