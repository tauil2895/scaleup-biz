"""
Django development settings for ScaleUp Biz project.
"""

from .base import *

DEBUG = True

# Internal IPs needed to render development tools like django-debug-toolbar
INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
]

# Add development-only apps and tools
INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# Development CORS permissions policy
CORS_ALLOW_ALL_ORIGINS = True

# Standard Email Console Backend to mock traffic without a real server
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"