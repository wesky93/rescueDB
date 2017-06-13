"""
Django settings for rescueDB project.

Generated by 'django-admin startproject' using Django 1.11.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ini파일 호출
from configparser import RawConfigParser

config = RawConfigParser()
config.read(os.path.join(BASE_DIR, 'settings.ini'))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.get('deploy', 'SECRET_KEY')


if config.get('deploy', 'DEBUG') == "True":
    DEBUG = True
elif config.get('deploy', 'DEBUG') == "False":
    DEBUG = False

ALLOWED_HOSTS = [config.get('deploy', 'ALLOWED_HOSTS')]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'record',
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

ROOT_URLCONF = 'rescueDB.urls'

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

WSGI_APPLICATION = 'rescueDB.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config.get('db', 'ENGINE'),
        'NAME': config.get('db', 'NAME'),
        'USER': config.get('db', 'USER'),
        'PASSWORD': config.get('db', 'PASSWORD'),
        'HOST': config.get('db', 'HOST'),
        'POST': config.get('db', 'POST'),
    }
}



# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# 한국 설정
LANGUAGE_CODE = config.get('language', 'LANGUAGE_CODE')
TIME_ZONE = config.get('language', 'TIME_ZONE')

USE_I18N = True

USE_L10N = True

USE_TZ = True

## 템플릿 파일 설정
TEMPLATES_DIRS = [os.path.join(BASE_DIR, 'templates')]
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# s3 스토리지 설정(참고 - https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_STORAGE_BUCKET_NAME = config.get('s3','BUCKET')
AWS_AUTO_CREATE_BUCKET = True
AWS_ACCESS_KEY_ID = config.get('s3','ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config.get('s3','SECRET_ACCESS_KEY')

AWS_S3_REGION_NAME = config.get('s3','S3_REGION_NAME')
AWS_S3_CUSTOM_DOMAIN =config.get('s3','CLOUDFRONT_DOMAIN')
