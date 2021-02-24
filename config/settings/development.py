import iptools

from .base import *  # noqa: F401

DEBUG = True

INTERNAL_IPS = iptools.IpRangeList(
    '10/8',
    '127/8',
    '172.16/12',
    '192.168/16'
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS.append('debug_toolbar')

MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
