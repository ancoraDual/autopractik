"""
Django settings for autopractik project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&j4+@e*epc_rowf36r43e-yy@i%f0fuujn6=chu)(5ujv(uw^v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'autopractik',
    'autoescuelas',
    'alumnos',
    'profesores',
    'userprofiles',
    'jfu',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


# TEMPLATE_CONTEXT_PROCESSORS = (
#      "django.core.context_processors.request", # <- HERE
#      "django.contrib.auth.context_processors.auth",
#      # "django.core.context_processors.debug",
#      # "django.core.context_processors.i18n",
#      # "django.core.context_processors.media",
#      "django.core.context_processors.static",
#      # "django.core.context_processors.tz",
#      # "django.contrib.messages.context_processors.messages",
# )

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request', # <- HERE
    'autoescuelas.context_processors.basico',
)


ROOT_URLCONF = 'autopractik.urls'

WSGI_APPLICATION = 'autopractik.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-ES'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static/media')

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static/static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

UPLOAD_DIR='/autoescuelas/'

AUTHENTICATION_BACKENDS = {
    'userprofiles.backends.EmailBackend',
    'alumnos.backends.AlumnoAuthBackend',

}

# EMAIL

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.1and1.es'
EMAIL_PORT = '25'
EMAIL_HOST_USER = 'sergi@osipyme.com'
EMAIL_HOST_PASSWORD = '677616104'
EMAIL_USE_TLS = True





