"""Development settings and globals."""

from .base import *


########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
ENABLE_DEBUG_TOOLBAR=False
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


#DEBUG_TOOLBAR_PATCH_SETTINGS = False
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
if ENABLE_DEBUG_TOOLBAR:
    DEBUG_TOOLBAR_PATCH_SETTINGS = False
    ########## TOOLBAR CONFIGURATION
    #you must declare this before! Cache settings... very tricky things :-)
    # See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
    INTERNAL_IPS = ('127.0.0.1','localhost:8000')

    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }

    DEBUG_TOOLBAR_PANELS = [
        #default panels
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        #'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        #'debug_toolbar.panels.redirects.RedirectsPanel',

        #~ #extenions
        #~ #'debug_toolbar.panels.profiling.ProfilingPanel',
        'template_timings_panel.panels.TemplateTimings.TemplateTimings',
        'memcache_toolbar.panels.memcache.MemcachePanel',
    ]
    ########## END TOOLBAR CONFIGURATION

    #create this: manage.py createcachetable cache_table

    import memcache_toolbar.panels.memcache



    INSTALLED_APPS += (
        'debug_toolbar',
        'template_timings_panel',
        'memcache_toolbar',
    )

CACHES = {
        'dummy': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        },
        'sqlitecache': {
            'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
            'LOCATION': 'cache_table',
        },
        'systemmem': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            #'LOCATION': 'unique-snowflake',
        },
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            #'BACKEND':'django.core.cache.backends.memcached.PyLibMCCache',
            #'LOCATION': 'unix:/home/ripmeer/run/mem.sock',
            'LOCATION': 'unix:/var/run/memcached/memcached.sock',
            'TIMEOUT': 1, #5min
            'OPTIONS': {
                'MAX_ENTRIES': 1000
            }
        }
    }
CACHE_MIDDLEWARE_SECONDS=600
CACHE_MIDDLEWARE_ALIAS='dummy' #which cache to use
INSTALLED_APPS += (
        'django_extensions',
)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'standard': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter':'standard',
        },
         'sqlfile': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': './logs/sql.log',
        },
        'logfile': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': './logs/debug.log',
            'maxBytes': 50000,
            'backupCount': 2,
            'formatter':'standard',
        },

    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins','console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends':{
            'handlers':['sqlfile'],
            'level': 'DEBUG',
        },
        'banpy': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
        },
    }
}
