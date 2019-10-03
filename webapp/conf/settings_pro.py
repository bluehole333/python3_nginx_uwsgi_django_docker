from conf.settings import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE'),
        'USER': os.environ.get('MYSQL_USER'),
        'HOST': os.environ.get('MYSQL_HOST', '127.0.0.1'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD'),
        "PORT": os.environ.get('MYSQ_PORT', 3306),
    },
}
