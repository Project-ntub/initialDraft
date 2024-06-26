import logging
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y&%10_w2a%0v)(jqe46d2)mevjv0f^ro8!#+pu#67d%md8k8vr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'localhost', '140.131.114.158']

# Two-Factor Authentication settings
TWO_FACTOR_REMEMBER_COOKIE_AGE = 30 * 24 * 60 * 60  # 30天有效期

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_otp',
    'django_otp.plugins.otp_totp',
    'django_otp.plugins.otp_static',
    'two_factor',
    'app113209',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'app113209.middleware.allow_iframe.AllowIframeMiddleware',
]

ROOT_URLCONF = 'project113209.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'project113209.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 使用 MySQL 數據庫
        'NAME': '113-ntub113209',                 # 數據庫名稱
        'USER': 'ntub113209',                     # MySQL 用戶名
        'PASSWORD': 'Sw@23110565',             # MySQL 用戶密碼
        'HOST': '140.131.114.242',                  # 數據庫地址
        'PORT': '3306',                       # 數據庫端口
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'app113209.validators.CustomPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# login
# 對於前台
LOGIN_URL = '/frontend/login/'
LOGIN_REDIRECT_URL = '/frontend/home/'
LOGOUT_REDIRECT_URL = '/frontend/login/'

# 對於後台
BACKEND_LOGIN_URL = '/backend/login/'
BACKEND_LOGIN_REDIRECT_URL = '/backend/management/'
BACKEND_LOGOUT_REDIRECT_URL = '/backend/login/'

AUTH_USER_MODEL = 'app113209.User'

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
)


# Email settings for password reset and verification
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '11236017@ntub.edu.tw'
EMAIL_HOST_PASSWORD = 'cxur tzpv jiwm yytp'

# Session settings
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 60 * 30  # 30 分鐘
SESSION_COOKIE_SECURE = False  # 在本地開發時可以設定為 False，生產環境應設定為 True

# Cache settings
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

# 認證後端
AUTHENTICATION_BACKENDS = (
    'two_factor.auth_backend.TwoFactorBackend',
    'django.contrib.auth.backends.ModelBackend',
)
