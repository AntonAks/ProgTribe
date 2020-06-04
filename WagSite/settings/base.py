"""
Django settings for {{ project_name }} project.

<<<<<<< HEAD:venv/lib/python3.8/site-packages/wagtail/project_template/project_name/settings/base.py
Generated by 'django-admin startproject' using Django {{ django_version }}.

For more information on this file, see
https://docs.djangoproject.com/en/{{ docs_version }}/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/
=======
Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
>>>>>>> 74d6f5eb882f1ffdc6bc6b8567a308e507f4ed77:WagSite/settings/base.py
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
<<<<<<< HEAD:venv/lib/python3.8/site-packages/wagtail/project_template/project_name/settings/base.py
# See https://docs.djangoproject.com/en/{{ docs_version }}/howto/deployment/checklist/
=======
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/
>>>>>>> 74d6f5eb882f1ffdc6bc6b8567a308e507f4ed77:WagSite/settings/base.py


# Application definition

INSTALLED_APPS = [
    'home',
    'search',
<<<<<<< HEAD:venv/lib/python3.8/site-packages/wagtail/project_template/project_name/settings/base.py
=======

    'blog',
    'wagtailcodeblock',
>>>>>>> 74d6f5eb882f1ffdc6bc6b8567a308e507f4ed77:WagSite/settings/base.py

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',

    'modelcluster',
    'taggit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

<<<<<<< HEAD:venv/lib/python3.8/site-packages/wagtail/project_template/project_name/settings/base.py
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = '{{ project_name }}.urls'
=======
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

WAGTAIL_CODE_BLOCK_THEME = 'coy'
WAGTAIL_CODE_BLOCK_LANGUAGES = (
    ('bash', 'Bash/Shell'),
    ('css', 'CSS'),
    ('diff', 'diff'),
    ('html', 'HTML'),
    ('javascript', 'Javascript'),
    ('json', 'JSON'),
    ('python', 'Python'),
    ('scss', 'SCSS'),
    ('yaml', 'YAML'),
    ('r', 'R'),
)

ROOT_URLCONF = 'WagSite.urls'
>>>>>>> 74d6f5eb882f1ffdc6bc6b8567a308e507f4ed77:WagSite/settings/base.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = '{{ project_name }}.wsgi.application'


# Database
<<<<<<< HEAD:venv/lib/python3.8/site-packages/wagtail/project_template/project_name/settings/base.py
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases
=======
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
>>>>>>> 74d6f5eb882f1ffdc6bc6b8567a308e507f4ed77:WagSite/settings/base.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
<<<<<<< HEAD:venv/lib/python3.8/site-packages/wagtail/project_template/project_name/settings/base.py
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#auth-password-validators
=======
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
>>>>>>> 74d6f5eb882f1ffdc6bc6b8567a308e507f4ed77:WagSite/settings/base.py

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
<<<<<<< HEAD:venv/lib/python3.8/site-packages/wagtail/project_template/project_name/settings/base.py
# https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/
=======
# https://docs.djangoproject.com/en/3.0/topics/i18n/
>>>>>>> 74d6f5eb882f1ffdc6bc6b8567a308e507f4ed77:WagSite/settings/base.py

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
<<<<<<< HEAD:venv/lib/python3.8/site-packages/wagtail/project_template/project_name/settings/base.py
# https://docs.djangoproject.com/en/{{ docs_version }}/howto/static-files/
=======
# https://docs.djangoproject.com/en/3.0/howto/static-files/
>>>>>>> 74d6f5eb882f1ffdc6bc6b8567a308e507f4ed77:WagSite/settings/base.py

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# Javascript / CSS assets being served from cache (e.g. after a Wagtail upgrade).
<<<<<<< HEAD:venv/lib/python3.8/site-packages/wagtail/project_template/project_name/settings/base.py
# See https://docs.djangoproject.com/en/{{ docs_version }}/ref/contrib/staticfiles/#manifeststaticfilesstorage
=======
# See https://docs.djangoproject.com/en/3.0/ref/contrib/staticfiles/#manifeststaticfilesstorage
>>>>>>> 74d6f5eb882f1ffdc6bc6b8567a308e507f4ed77:WagSite/settings/base.py
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Wagtail settings

<<<<<<< HEAD:venv/lib/python3.8/site-packages/wagtail/project_template/project_name/settings/base.py
WAGTAIL_SITE_NAME = "{{ project_name }}"
=======
WAGTAIL_SITE_NAME = "WagSite"
>>>>>>> 74d6f5eb882f1ffdc6bc6b8567a308e507f4ed77:WagSite/settings/base.py

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://example.com'
