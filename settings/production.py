from .base import *

DEBUG = False

ALLOWED_HOSTS = ['arshidi.com', 'www.arshidi.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'isitnowr_thisisthedatabaseofarshidicrm',
        'USER': 'isitnowr_usernameofarshidicrmwebapp',
        'PASSWORD': '[@cnY.gkFv&d(kM8Pp',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
