"""
Django settings for Python Anywhere project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

ON_PYTHON_ANYWHERE = False
if os.getcwd() == '/home/lastmj':
    ON_PYTHON_ANYWHERE = True

#ON_OPENSHIFT = False TODO change this to check if we are on python anywhere
#if os.environ.has_key('OPENSHIFT_REPO_DIR'):
#     ON_OPENSHIFT = True

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'ascq#%bii8(tld52#(^*ht@pzq%=nyb7fdv+@ok$u^iwb@2hwh'

default_keys = { 'SECRET_KEY': 'vm4rl5*ymb@2&d_(gc$gb-^twq9w(u69hi--%$5xrh!xk(t%hw' }
use_keys = default_keys

#if ON_OPENSHIFT: TODO change this to check if we are on python anywhere
#     imp.find_module('openshiftlibs')
#     import openshiftlibs
#     use_keys = openshiftlibs.openshift_secure(default_keys)

SECRET_KEY = use_keys['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
if ON_PYTHON_ANYWHERE:
     DEBUG = True
else:
     DEBUG = True

TEMPLATE_DEBUG = DEBUG

if DEBUG:
     ALLOWED_HOSTS = []
else:
     ALLOWED_HOSTS = ['www.solutiamaxima.com']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'createproblem',
    'publicproblem',
    'publicworkspace',
    'customauthentication',
    'privateworkshop',
)

MIDDLEWARE_CLASSES = (
    'sslify.middleware.SSLifyMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# If you want configure the REDISCLOUD
if 'REDISCLOUD_URL' in os.environ and 'REDISCLOUD_PORT' in os.environ and 'REDISCLOUD_PASSWORD' in os.environ:
    redis_server = os.environ['REDISCLOUD_URL']
    redis_port = os.environ['REDISCLOUD_PORT']
    redis_password = os.environ['REDISCLOUD_PASSWORD']
    CACHES = {
        'default' : {
            'BACKEND' : 'redis_cache.RedisCache',
            'LOCATION' : '%s:%d'%(redis_server,int(redis_port)),
            'OPTIONS' : {
                'DB':0,
                'PARSER_CLASS' : 'redis.connection.HiredisParser',
                'PASSWORD' : redis_password,
            }
        }
    }
    MIDDLEWARE_CLASSES = ('django.middleware.cache.UpdateCacheMiddleware',) + MIDDLEWARE_CLASSES + ('django.middleware.cache.FetchFromCacheMiddleware',)

ROOT_URLCONF = 'urls'

#WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
     os.path.join(BASE_DIR,'templates'),
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
if ON_PYTHON_ANYWHERE:
     DATABASES = {
         'default': {
		    'ENGINE': 'django.db.backends.mysql',
		    'NAME': 'lastmj$solutiamaxima',
		    'USER': 'lastmj',
		    'PASSWORD': 'solmaxutiaima5010',
		    'HOST': 'mysql.server',
         }
     }
else:
     DATABASES = {
         'default': {
		    'ENGINE': 'django.db.backends.mysql',
		    'NAME': 'solutiamaxima',
		    'USER': 'root',
		    'PASSWORD': 'solmaxutiaima5010',
		    'HOST': '',
		    'PORT': '',
         }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'server-static')
STATIC_URL = '/static/'
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
