"""
Django settings
"""

import os
from pathlib import Path
from json import load
import environ

BASE_DIR = Path(__file__).resolve().parent

ENV = environ.Env()
ENV.read_env()

SECRET_KEY = ENV("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = [
    ENV("VPS_IP_ADDRESS"),
    "127.0.0.1",
    "www.calebrichardson.dev",
    "calebrichardson.dev",
    "localhost",
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "me_info",
    "demos.personal_finance_automated",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "me_info", "templates", "me_info"),
            os.path.join(
                BASE_DIR,
                "demos",
                "personal_finance_automated",
                "templates",
                "personal_finance_automated",
            ),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
WSGI_APPLICATION = "wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": ENV("DB_NAME"),
        "USER": ENV("DB_CONN_USER"),
        "PASSWORD": ENV("DB_CONN_PASS"),
        "HOST": ENV("DB_IP_ADDRES"),
        "PORT": "5432",
    }
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": BASE_DIR / "db.sqlite3",
    # }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "me_info/static"),
    os.path.join(BASE_DIR, "demos/personal_finance_automated/static"),
]
MEDIA_URL = "IMG/"
JSON_PATH = os.path.join(BASE_DIR, "me_info", "static", "JSON", "")
CSV_PATH = os.path.join(
    BASE_DIR, "demos", "personal_finance_automated", "static", "CSV"
)

SESSION_SAVE_EVERY_REQUEST = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
# session age lasts for 12 hours
SESSION_COOKIE_AGE = 43200

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

if ENV("APP_ENV") == "development":
    print("dev")
    DEBUG = True

if ENV("APP_ENV") == "production":
    print("prod")
    DEBUG = False
