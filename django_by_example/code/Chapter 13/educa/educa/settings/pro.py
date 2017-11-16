from .base import *

DEBUG = False

ADMINS = {
    ('Antonio M', 'email@mydomain.com'),
}

ALLOWED_HOSTS = ['educaproject.com', 'www.educaproject.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': '****',
    }
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True