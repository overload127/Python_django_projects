DEBUG = False
ALLOWED_HOSTS = ['192.168.1.147',]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_shop',
        'USER': 'django_shop',
        'PASSWORD': 'django_shop',
        'HOST': 'localhost',
        'PORT': '',
    }
}
