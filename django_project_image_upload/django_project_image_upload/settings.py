"""
Django settings for django_project_image_upload project.

This file contains the configuration settings for your Django project.
It defines various parameters that control the behavior of your application,
such as database settings, installed apps, middleware, templates, static files,
and more.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

import os
from dotenv import load_dotenv
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file
# This should be done before accessing any environment variables
load_dotenv(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
# IMPORTANT: Never use the default SECRET_KEY in production. Generate a strong, unique secret key.
# For development, you can use a simple key, but for production, generate a random one.
# You can generate a secret key using the following command:
# python -c "import secrets; print(secrets.token_urlsafe(50))"
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# Set DEBUG to False in production for security reasons.
# Change to False in production
DEBUG = True

# ALLOWED_HOSTS: Define allowed hostnames for your application in production.
# This prevents Host Header Injection attacks.
# Add your production domain(s) here
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin', # Django's built-in admin interface
    'django.contrib.auth', # Django's authentication system
    'django.contrib.contenttypes', # Django's content types framework
    'django.contrib.sessions', # Django's session framework
    'django.contrib.messages', # Django's messaging framework
    'django.contrib.staticfiles', # Django's static files framework. Enable static file handling
    'app_image_upload', # Your custom app for image uploads
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware', # Handles various security aspects
    'django.contrib.sessions.middleware.SessionMiddleware', # Manages user sessions
    'django.middleware.common.CommonMiddleware', # Provides common middleware functionalities
    'django.middleware.csrf.CsrfViewMiddleware', # Protects against Cross-Site Request Forgery attacks
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Handles user authentication
    'django.contrib.messages.middleware.MessageMiddleware', # Handles messages displayed to users
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # Protects against clickjacking attacks
]

ROOT_URLCONF = 'django_project_image_upload.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', # Django's template engine
        'DIRS': [], # Add template directories here if needed
        'APP_DIRS': True, # Look for templates in apps' 'templates' directory
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug', # Adds debug information to templates
                'django.template.context_processors.request', # Adds the request object to templates
                'django.contrib.auth.context_processors.auth', # Adds authentication information to templates
                'django.contrib.messages.context_processors.messages', # Adds messages to templates
            ],
        },
    },
]

WSGI_APPLICATION = 'django_project_image_upload.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
# For production, consider using a more robust database like PostgreSQL or MySQL.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # SQLite database engine. SQLite is suitable for development
        'NAME': BASE_DIR / 'db.sqlite3', # Path to the SQLite database file
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', # Checks for password similarity with user attributes
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', # Checks for minimum password length
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', # Checks for common passwords
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', # Checks for numeric passwords
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/
LANGUAGE_CODE = 'en-us' # Default language code (English)
TIME_ZONE = 'UTC' # Default time zone (UTC)
USE_I18N = True # Enable internationalization and localization
USE_TZ = True # Enable time zone awareness

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
# URL for static files
STATIC_URL = '/static/' # URL for accessing static files
STATIC_ROOT = BASE_DIR / 'staticfiles' # Directory where static files will be collected

# Media files (User uploaded files)
MEDIA_URL = '/media/' # URL for accessing media files
MEDIA_ROOT = BASE_DIR / 'media' # Directory where media files will be stored

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' # Default primary key field type

# Amazon S3 configuration
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID') # AWS access key ID
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY') # AWS secret access key
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME') # AWS S3 bucket name
AWS_S3_REGION_NAME = os.environ.get('AWS_S3_REGION_NAME') # AWS S3 region name
AWS_DEFAULT_ACL = None # Default ACL for S3 objects. You can set specific ACLs if needed.  None is generally fine.
AWS_S3_SIGNATURE_VERSION = 's3v4' # AWS S3 signature version

# Configure file storage to use S3 for both static and media files
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage' # Storage backend for media files
# Use S3 for static files as well
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage' # Storage backend for static files