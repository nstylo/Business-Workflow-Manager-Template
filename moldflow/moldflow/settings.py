"""
Django settings for ***REMOVED*** project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
DJANGO_ENV = os.getenv("DJANGO_ENV")

# these env vars should be set in your django venv activate file
# or .env in production
if DJANGO_ENV == "development":
    DEBUG = True
    ALLOWED_HOSTS = ["*"]
    CORS_ORIGIN_WHITELIST = ["http://127.0.0.1:3000", "http://localhost:3000"]
    CSRF_COOKIE_SECURE = False
    SESSION_COOKIE_SECURE = False

    # to run email locally:
    # python -m smtpd -n -c DebuggingServer localhost:1025
    EMAIL_HOST = "localhost"
    EMAIL_PORT = "1025"
    EMAIL_HOST_USER = "test@gmail.com"
    EMAIL_HOST_PASSWORD = None
else:  # deployment env
    DEBUG = False
    ALLOWED_HOSTS = [os.getenv("HOST")]
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    # email
    EMAIL_HOST = os.getenv("EMAIL_HOST")
    EMAIL_PORT = os.getenv("EMAIL_PORT")
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

CSRF_COOKIE_NAME = "csrftoken"

SECURE_HSTS_SECONDS = 360  # time out non https users
SECURE_CONTENT_TYPE_NOSNIFF = True  # prevent user uploaded file sniffing
SECURE_BROWSER_XSS_FILTER = True  # cross site scripting protection
X_FRAME_OPTIONS = "DENY"  # clickjacking protection
SECURE_HSTS_PRELOAD = True  # submit site to browser preload list
# prevent attack on subdomain from insecure connection
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Application definition

INSTALLED_APPS = [
    "django.contrib.auth",
    "jet.dashboard",
    "jet",
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "rest_registration",
    "phonenumber_field",
    "users.apps.UsersConfig",
    "jobs",
]

# see https://github.com/stefanfoulis/django-phonenumber-field
PHONENUMBER_DB_FORMAT = "INTERNATIONAL"

AUTH_USER_MODEL = "users.CustomUser"  # our custom user model

CORS_ALLOW_CREDENTIALS = True  # to allow csrf session cookies

CORS_URLS_REGEX = r"^/api/.*$"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "***REMOVED***.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

# name of our wsgi application to run with gunicorn
WSGI_APPLICATION = "***REMOVED***.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
DB_NAME = os.getenv("DB_NAME")
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": DB_NAME,
        "USER": POSTGRES_USER,
        "PASSWORD": POSTGRES_PASSWORD,
        "HOST": POSTGRES_HOST,
        "PORT": POSTGRES_PORT,
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LOGIN_REDIRECT_URL = "/"

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication"
    ],
    "DEFAULT_THROTTLE_CLASSES": ["rest_framework.throttling.UserRateThrottle"],
    "DEFAULT_THROTTLE_RATES": {"user": "10/minute"},
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
}

REST_REGISTRATION = {
    "REGISTER_VERIFICATION_ENABLED": True,
    "REGISTER_EMAIL_VERIFICATION_ENABLED": True,
    "RESET_PASSWORD_VERIFICATION_ENABLED": True,
    "VERIFICATION_FROM_EMAIL": EMAIL_HOST_USER,
    # TODO: route frontend urls
    # https://django-rest-registration.readthedocs.io/en/latest/detailed_configuration/register.html#verification-workflow
    "REGISTER_VERIFICATION_URL": "http://127.0.0.1:8000/",
    "REGISTER_EMAIL_VERIFICATION_URL": "http://127.0.0.1:8000/",
    # https://django-rest-registration.readthedocs.io/en/latest/detailed_configuration/reset_password.html
    "RESET_PASSWORD_VERIFICATION_URL": "http://127.0.0.1:8000/",
    "USER_HIDDEN_FIELDS": (
        "is_active",
        "is_admin",
        "is_staff",
        "is_superuser",
        "user_permissions",
        "groups",
        "date_joined",
    ),
}

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Amsterdam"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
MEDIA_URL = "/django_media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATIC_URL = "/django_static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
