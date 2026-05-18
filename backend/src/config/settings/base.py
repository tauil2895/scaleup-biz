"""
Django base settings for ScaleUp Biz project.
"""

from pathlib import Path
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Adjusting to look 3 levels up to hit backend/ directory from config/settings/
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Initialize environment variables loader
env = environ.Env()

# ------------------------------------------------------------------------------
# Core Security Baseline
# ------------------------------------------------------------------------------
SECRET_KEY = env.str("SECRET_KEY")
DEBUG = env.bool("DEBUG", default=False)
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])

# ------------------------------------------------------------------------------
# Application Definitions
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "django_filters",
    "corsheaders",
    "drf_spectacular",
]

LOCAL_APPS = [
    # Custom business domain apps under src/modules/ go here later
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# ------------------------------------------------------------------------------
# Middleware Chains
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ------------------------------------------------------------------------------
# Database Configurations Template
# ------------------------------------------------------------------------------
DATABASES = {
    "default": env.db("DB_URL", default=f"{env.str('DB_ENGINE')}://{env.str('DB_USER')}:{env.str('DB_PASSWORD')}@{env.str('DB_HOST')}:{env.str('DB_PORT')}/{env.str('DB_NAME')}")
}

# ------------------------------------------------------------------------------
# Internationalization & Localization
# ------------------------------------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ------------------------------------------------------------------------------
# Static and Media Files Assets Management
# ------------------------------------------------------------------------------
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "mediafiles"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ------------------------------------------------------------------------------
# REST Framework Configuration Baseline
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.NamespaceVersioning",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "ScaleUp Biz SaaS API",
    "DESCRIPTION": "Enterprise Marketplace API for Small Business Services",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}