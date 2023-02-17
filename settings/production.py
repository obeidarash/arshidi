from .base import *

DEBUG = False

ALLOWED_HOSTS = ['crm.arshidi.com', 'www.crm.arshidi.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'isitnowr_crmdatabaseofarshidi',
        'USER': 'isitnowr_arshidiusernamecrm',
        'PASSWORD': 'Qum2OnkD^ZG02i62.P',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
