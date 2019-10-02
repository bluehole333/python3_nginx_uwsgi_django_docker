from conf.settings import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'HOST': '127.0.0.1',
        'PASSWORD': 'django',
        # "PORT": 3307,
    },
}
