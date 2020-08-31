'''Default Settings'''
from base import *
from django.core.files.storage import FileSystemStorage

########## EMAIL CONFIGURATION
#settings on hoster

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST='localhost'
#EMAIL_PORT=587
#EMAIL_USE_TLS=True

#EMAIL_HOST_USER='mail@example.de'
#EMAIL_HOST_PASSWORD='H0Nullutella34'

#EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME
#EMAIL_SEND_TO=['meertec@tucana.hoster.de',EMAIL_HOST_USER,]
#SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION

########## DATABASE CONFIGURATION
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': 'django',
#        'USER': 'django',
#        'PASSWORD': 'c>;teL40QLNeM?{@>VlIhJc&Ay)(8v]mkk.G]vshG!~G>O-Btk^R>nvAWe_Ijh%KMPIfRF[[?,SpI!8#44Jud/WPr4"db:H~ege',
#        'HOST': '/home/ripmeer/tmp/',
#        'PORT': '',
#    }
#}
########## END DATABASE CONFIGURATION

ADMINS = (
    ('meertec','mail@example.de'),
)

ALLOWED_HOSTS = ['.hamal.hoster.de',
        '.hamal.hoster.de.',
]

INSTALLED_APPS += (
    'djangosecure',
)


STATIC_ROOT = '/var/www/virtual/meertec0/html/static'
MEDIA_ROOT = '/var/www/virtual/meertec0/html/media'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        #'BACKEND':'django.core.cache.backends.memcached.PyLibMCCache',
        #'LOCATION': 'unix:/home/ripmeer/run/mem.sock',
        'LOCATION': 'unix:/home/meertec0/run/memcached.sock',
        'TIMEOUT': 300, #5min
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}

CACHE_MIDDLEWARE_SECONDS=600 #secodns each site will be cached
CACHE_MIDDLEWARE_ALIAS='default' #which cache to use

MIDDLEWARE_CLASSES += (
    #django-secure
    'djangosecure.middleware.SecurityMiddleware',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}


########## COMPRESSION CONFIGURATION
# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE
COMPRESS_OFFLINE = True

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_STORAGE
#COMPRESS_STORAGE = FileSystemStorage

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_CSS_FILTERS
COMPRESS_CSS_FILTERS += [
    'compressor.filters.cssmin.CSSMinFilter',
]

# See: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_JS_FILTERS
COMPRESS_JS_FILTERS += [
    'compressor.filters.jsmin.JSMinFilter',
]
########## END COMPRESSION CONFIGURATION

########## Security Options
#if HTTPS is enabled, will be send cookies only over https
SESSION_COOKIE_SECURE=True
SESSION_COOKIE_HTTPONLY=True
#redirect all http to https, check if you have a valid certificate!
SECURE_SSL_REDIRECT=True
#HTTP Strict Transport Secruity
SECURE_HSTS_SECONDS=1000
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
#prevent framing of your pages
SECURE_FRAME_DENY=True
#prevent the browser from guessing asset content types
SECURE_CONTENT_TYPE_NOSNIFF=True
#enable the browser’s XSS filtering protections
SECURE_BROWSER_XSS_FILTER=True
#running checks with: ./manage.py checksecure
########## END SECURITY
