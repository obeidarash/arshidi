from .base import *

DEBUG = False

ALLOWED_HOSTS = ['arshidi.com', 'www.arshidi.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'isitnowr_arshididatabase',
        'USER': 'isitnowr_arshidiusername',
        'PASSWORD': 'jTudjgNk7eHH',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
