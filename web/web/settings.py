"""
Django settings for web project.

Generated by 'django-admin startproject' using Django 1.11.17.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v6pbi)sqp#0)522w9pcz6ma&m2#m=i8o1z+l=j#3r$@bz9d1!m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myhome',
    'myadmin',
    'ueditor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #自定义的中间件--后台登录使用 -- 文件夹myadmin AdminMiddleware.py 类：AdminLoginMiddleware
    'myadmin.views.AdminMiddleware.AdminLoginMiddleware',
]

ROOT_URLCONF = 'web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cong', # 库名
        'USER': 'cong',
        'PASSWORD': '123456',
        'HOST': '192.168.9.37',
        'PORT': '3306',
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

LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


# 支付宝配置文件
# APPID
# 沙箱APPID，生产环境须更改为应用APPID。
ALIPAY_APPID = "2016100900648245"

# 网关
# 沙箱网关，生产环境须更改为正式网关。
ALIPAY_URL = "https://openapi.alipaydev.com/gateway.do"
# 正式网关，开发环境勿使用。---真实环境
# ALIPAY_URL = "https://openapi.alipay.com/gateway.do"

# 回调通知地址
# 如果只可以内网访问开发服务器
ALIPAY_NOTIFY_URL = "http://192.168.9.37/order/pay_result/"
# 如果生产环境或外网可以访问开发服务器
# ALIPAY_NOTIFY_URL = "http://1.203.45.678:8000/order/pay_result/"

# 支付后的跳转地址
ALIPAY_RETURN_URL = 'http://192.168.9.37/order/pay_success/'

# 应用私钥
APP_PRIVATE_KEY_PATH = os.path.join(BASE_DIR, 'keys/app_private_key.txt')
# 支付宝公钥
ALIPAY_PUBLIC_KEY_PATH = os.path.join(BASE_DIR, 'keys/alipay_public_key.txt')
