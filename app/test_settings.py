import os

import django

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")




from django.conf import settings
settings.configure()
django.setup()



LOCKDOWN_ADMIN = False
INSTALLED_APPS = [
    "contato.ContatoConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'contato',
    'api',
    'rest_framework',
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'