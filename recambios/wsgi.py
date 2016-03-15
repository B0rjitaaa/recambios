"""
WSGI config for recambios project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import recambios.wsgi

# Reuse recambios/wsgi
application = recambios.wsgi.application

