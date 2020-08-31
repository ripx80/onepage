"""Base settings and globals."""

from os.path import abspath,split,dirname,basename,join
import sys
from django.utils.translation import ugettext_lazy as _


ugettext = lambda s: s

########## PATH CONFIGURATION

# Set the Project path
PROJECT_PATH = split(abspath(dirname(__file__)))[0]
BASE_DIR=PROJECT_PATH
# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(PROJECT_PATH)

# Site name:
SITE_NAME = basename(PROJECT_PATH)
#SITE_NAME="Meertec"

LOCALE_PATHS = (join(PROJECT_PATH), 'locale/',)
MEDIA_ROOT = join(PROJECT_PATH, "media/")
STATIC_ROOT = join(PROJECT_PATH, "static/")

########## END PATH CONFIGURATION


########## DEBUG CONFIGURATION

DEBUG = False
TEMPLATE_DEBUG = DEBUG

########## END DEBUG CONFIGURATION


########## MANAGER CONFIGURATION

ADMINS = (
    ('mail','mail@example.de'),
)
MANAGERS = ADMINS

########## END MANAGER CONFIGURATION


########## DATABASE CONFIGURATION

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'project.sql',                      # Or path to database file if using sqlite3.
    }
}

########## END DATABASE CONFIGURATION

########## ADDITIONAL CONFIG

COPYRIGHT="ripx80ler"

########## END ADDITIONAL CONFIG


########## GENERAL CONFIGURATION

ALLOWED_HOSTS = ['localhost']
TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'en'
USE_I18N = True
USE_L10N = True
USE_TZ = True
SITE_ID = 1

########## END GENERAL CONFIGURATION

########## LOCALES CONFIGURATION


#the order is important for some apps :-)



LANGUAGES = (
  ('de', _('Deutsch')),
  ('en', _('English')),
)



# Additional locations of static files,use absolute path
STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',

    #django-compressor finder
    'compressor.finders.CompressorFinder',
)

########## FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    join(PROJECT_PATH, 'fixtures/'),
)
########## END FIXTURE CONFIGURATION

#change this for every project!!!
SECRET_KEY = 'u7x+*1bpwalkg(nbk=+w(c#aeh%j&_@)1dtq(5*^p*yj^$l@y&'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.app_directories.load_template_source',
    #'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS =(
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
     #for caching

    'django.middleware.cache.UpdateCacheMiddleware',    #cache
    #strip cookie from analytics -> todo

     # Use GZip compression to reduce bandwidth.
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #limit logins
    'apps.banpy.middleware.RateLimitMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware', #cache


)

MEDIA_URL = '/media/'
STATIC_URL = '/static/'
ROOT_URLCONF = 'apps.urls'
WSGI_APPLICATION = 'apps.wsgi.application'
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
TEMPLATE_DIRS = (
   join(PROJECT_PATH, "templates"),
   join(PROJECT_PATH, "templatetags"),
)

########## APP CONFIGURATION
DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #must inserted before admin
    'grappelli',

    'django.contrib.admin',
    'django.contrib.sitemaps',
    )

THIRD_PARTY_APPS = (
    # Database migration helpers:
    #'south',
    # Static file management:
    'compressor',
    #translation
    'hvad',
    #Editor Plugin
    'ckeditor',
    #Thumbnails
    'easy_thumbnails',
    'easy_thumbnails.optimize',
    #Shows Cookie Disclaimer
    'apps.cookie_banner',

)

LOCAL_APPS = (
    'apps.skin',
    'apps.onepage',
    #robots.txt handling#
    'apps.mt_robot',
    #Brute-Force Protection#
    'apps.banpy',
    'libs.bootstrap',
    'libs.jquery',

)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

########## LOGGING CONFIGURATION
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins','console','file'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
########## END LOGGING CONFIGURATION

########## COMPRESSION CONFIGURATION
# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_ENABLED
COMPRESS_ENABLED = True

# See: http://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_CSS_HASHING_METHOD
COMPRESS_CSS_HASHING_METHOD = 'content'

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_CSS_FILTERS
COMPRESS_CSS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
]

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_JS_FILTERS
COMPRESS_JS_FILTERS = [
    'compressor.filters.template.TemplateFilter',
]
########## END COMPRESSION CONFIGURATION

########## CKEDITOR CONFIGURATION
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_IMAGE_BACKEND = "pillow"
#CKEDITOR_JQUERY_URL #set this to jquery lib
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Advanced',
    },
}
########## END CKEDITOR CONFIGURATION

########## EASY_THUMBNAILS

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'easy_thumbnails.processors.scale_and_crop',
   # 'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
    'easy_thumbnails.processors.background',
)
SOUTH_MIGRATION_MODULES = {
     'easy_thumbnails': 'easy_thumbnails.south_migrations',
}

THUMBNAIL_ALIASES = {
    '': {
        'mp': {'size': (320, 480), 'crop': True,},
        'ml': {'size': (480, 320), 'crop': True},
        'sp': {'size': (600, 800), 'crop': True},
        'sl': {'size': (800, 600), 'crop': True},
        'tp': {'size': (768, 1024), 'crop': True},
        'tl': {'size': (1024, 768), 'crop': True},
        'dp': {'size': (1280, 720), 'crop': True},
    },
}
THUMBNAIL_QUALITY = 75
#Optimization
THUMBNAIL_OPTIMIZE_COMMAND = {
    'png': '/usr/bin/optipng {filename}',
    'gif': '/usr/bin/optipng {filename}',
    'jpeg': '/home/meertec0/bin/jpegoptim {filename}'
}
########## END EASY_THUMBNAILS

########## GRAPPELLI

GRAPPELLI_ADMIN_TITLE='Meertec Onepage'

########## END GRAPPELLI

########## RATELIMIT-BACKEND


AUTHENTICATION_BACKENDS = (
     'apps.banpy.backends.LimitLogin',
)

########## END RATELIMIT-BACKEND

########## ROBOTS

ROBOTS_USE_SITEMAP = True
ROBOTS_CACHE_TIMEOUT = 60*60*24
#~ ROBOTS_SITEMAP_URLS = [
    #~ 'http://www.example.com/sitemap.xml',
#~ ]
########## END ROBOTS

########### BANPY

BAN_TIME=1          #in minutes
BAN_REQUESTS = 3
BAN_IPBASED=True    # is based on ip not on username. better security but somtetimes evil ;-)
BAN_USE_IPTABLES=False    # ban the ip with iptables, for heavy stuff
########### END BANPY
