import os

from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(dotenv_path=BASE_DIR / ".env")

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-(l^y*xm_umz7lfx5j@k3ttgm*j5(rd94zl&$h+-zkrr9zu_wlo"
)
JWT_SECRET = os.getenv("JWT_SECRET", "inse")

DEBUG = False if os.getenv("DEBUG") == "False" else True

INTERNAL_IPS = [
    "127.0.0.1",
]

# CORS
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.ngrok-free.dev', '.ngrok.io']
CSRF_TRUSTED_ORIGINS = ['https://*.ngrok-free.dev', 'https://*.ngrok.io']

INSTALLED_APPS = [
    # server
    "daphne",

    # middleware
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "channels",
    "debug_toolbar",
    'cloudinary',
    'cloudinary_storage',

    # project apps
    "chat_app",
    "home_app",
    "notification_app",
    "post_app",
    "profile_app",
    "user_app",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "WorldITSocialNetwork.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
            BASE_DIR / "chat_app" / "templates",
            BASE_DIR / "home_app" / "templates",
            BASE_DIR / "post_app" / "templates",
            BASE_DIR / "profile_app" / "templates",
            BASE_DIR / "user_app" / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# cache
# TODO: add later redis
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "127.0.0.1:11211",
    }
}

# websockets
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}

# auth
LOGIN_URL = "user_app.auth"
AUTH_USER_MODEL = "user_app.User"

# asgi
ASGI_APPLICATION = "WorldITSocialNetwork.asgi.application"

# Database
if not os.getenv("REMOTE_DB_ENGINE"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    from sshtunnel import SSHTunnelForwarder

    if os.getenv("SSH_LOGIN"):
        tunnel = SSHTunnelForwarder(
            ('ssh.pythonanywhere.com', 22),
            ssh_username=os.getenv("SSH_LOGIN"),
            ssh_password=os.getenv("SSH_PASSWORD"),
            remote_bind_address=(os.getenv("REMOTE_DB_HOST"), int(os.getenv("REMOTE_DB_PORT"))), # type: ignore
        )

        tunnel.start()

        port = str(tunnel.local_bind_port)
    else:
        port = os.getenv("REMOTE_DB_PORT")

    if not os.getenv("DATABASE_URL"):
        DATABASES = {
            "default": {
                'ENGINE': os.getenv("REMOTE_DB_ENGINE"),
                'NAME': os.getenv("REMOTE_DB_NAME"),
                'USER': os.getenv("REMOTE_DB_USER"),
                'PASSWORD': os.getenv("REMOTE_DB_PASSWORD"),
                'HOST': '127.0.0.1', 
                'PORT': port,
                'CONN_MAX_AGE': 600
            }
        }
    else:
        import dj_database_url

        DATABASES = {
            'default': dj_database_url.config(
                default=os.getenv("DATABASE_URL"),
                conn_max_age=600,
                ssl_require=True 
            )
        }

# Password validation
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
LANGUAGE_CODE = "en-us"

TIME_ZONE = 'Europe/Kyiv'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
    BASE_DIR / "chat_app" / "static",
    BASE_DIR / "home_app" / "static",
    BASE_DIR / "notification_app" / "static",
    BASE_DIR / "post_app" / "static",
    BASE_DIR / "profile_app" / "static",
    BASE_DIR / "user_app" / "static",
]

# SMTP
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

# Media
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
STATIC_ROOT = BASE_DIR / "staticfiles"

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.getenv('CLOUDINARY_CLOUD_NAME'),
    "API_KEY": os.getenv('CLOUDINARY_API_KEY'),
    "API_SECRET": os.getenv('CLOUDINARY_API_SECRET')
}

STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage"
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}