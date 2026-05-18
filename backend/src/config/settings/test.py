"""
Django testing settings for ScaleUp Biz project.
"""

from .base import *

DEBUG = False

# Accelerate user authentication process during test assertions
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

# Direct in-memory email buffer isolation
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# Deactivate Celery synchronization delays during testing blocks
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True