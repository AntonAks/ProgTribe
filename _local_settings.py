# THIS FILE MUST BE RENAMED TO local_settings.py 


import os

### Global settings 
BASE_DIR = ''

SECRET_KEY = ''

DEBUG = ''

ALLOWED_HOSTS = []
INTERNAL_IPS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'WagSite/db.sqlite3'),
    }
}


### Web settings

WEB_CUSTOM_META = {
    "web_site_name": "Welcome to WagSite",
}