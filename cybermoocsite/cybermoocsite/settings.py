from pathlib import Path
# import os Fix Flaw 4

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o$xys1f*&=!2f9mp)5liv00k05+hu$tmgm0r9hhv(8b+ul&*%^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True' Fix flaw 4

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'cyberapp.apps.CyberappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cybermoocsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'cybermoocsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

"""
 LOGGING = {
     "version": 1,
     "disable_existing_loggers": False,
     "formatters": {
         "verbose": {
             "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
             "datefmt": "%Y-%m-%d_%H:%M:%S",
             "style": "{",
         },
         "simple": {
             "format": "{levelname} {message}",
             "style": "{",
         },
     },
     "handlers": {
         "file": {
             "level": "INFO",
             "class": "logging.handlers.TimedRotatingFileHandler",
             "formatter": "verbose",
             "filename": "./logs/cyberapp.log",
             "when": "midnight",
             "interval": 1,
             "backupCount": 5,
             "encoding": None,
             "delay": False,
             "utc": False,
             "atTime": None,
             "errors": None,
         },
         "console": {
             "level": "INFO",
             "class": "logging.StreamHandler",
             "formatter": "simple",
         },
     },
     "loggers": {
         "django": {
             "handlers": ["console"],
             "propagate": True,
         },
         "": {
             "handlers": ["file"],
             "level": "INFO",
         },
     },
 }
"""
# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
