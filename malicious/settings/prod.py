import os
from malicious.settings.base import *
from malicious.settings.base import BASE_DIR



ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS = ['https://'+os.environ['WEBSITE_HOSTNAME']]
DEBUG = False
SECRET_KEY = os.environ['MY_SECRET_KEY']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
]

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

CONNECTION = os.environ['AZURE_POSTGRESQL_CONNECTIONSTRING']
CONNECTION_STRING = {pair.split('=')[0]: pair.split('=')[1] for pair in CONNECTION.split(' ')}

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': CONNECTION_STRING['dbname'],
    #     'USER': CONNECTION_STRING['user'],
    #     'PASSWORD': CONNECTION_STRING['password'],
    #     'HOST': CONNECTION_STRING['host'],
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'kuma0997_malicious',
        'USER': 'kuma0997_aiteca',
        'PASSWORD': 'Od]ys0_MpBlB',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

STATIC_ROOT = BASE_DIR/'staticfiles'