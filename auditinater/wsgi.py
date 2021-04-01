# Import order important here. Get logging set up before importing django.
import os

from django.core.wsgi import get_wsgi_application

from auditinater import botlogging


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auditinater.settings")

botlogging.log_setup()

application = get_wsgi_application()
