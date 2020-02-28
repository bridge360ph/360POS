"""
Production use of settings
"""

from . base import *

DEBUG = False

ALLOWED_HOSTS = ['.pythonanywhere.com']

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bridge360pos$pos',
        'USER': 'bridge360pos',
        'PASSWORD': 'fishmond22',
        'HOST': 'bridge360pos.mysql.pythonanywhere-services.com',
        'PORT': 3306,
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'; \
                            SET foreign_key_checks = 0",
        },
    }
}

# see https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_ROOT = (
    os.path.join(ROOT_DIR, 'staticfiles')
)

# SSL/TLS SETTINGS FOR DJANGO
CORS_REPLACE_HTTPS_REFERER = True
HOST_SCHEME = "https://"
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SECURE_SSL_HOST = True
SECURE_HSTS_SECONDS = 1000000
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

CSRF_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_FRAME_DENY = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
