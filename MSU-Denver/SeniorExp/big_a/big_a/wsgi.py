"""
WSGI config for big_a project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import os, sys
sys.path.append('/Users/chrii/Desktop/MSU-Denver/SeniorExp/big_a')
sys.path.append('/MSU-Denver/SeniorExp/myprojectenv/lib/python3.12/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "big_a.settings")

path = '/var/www/diffior_pythonanywhere_com_wsgi.py'
if path not in sys.path:
    sys.path.append(path)

os.environ['big_a.settings'] = 'mysite.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

application = get_wsgi_application()
