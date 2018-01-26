"""
Django settings for lqcharacter2 project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import sys
import os
import os.path
from django.utils import six
from django.utils.translation import ugettext_lazy as _

# Python的最大递归深度错误
# http://leyex.blog.51cto.com/4230949/1884041
# https://cyrusin.github.io/2015/12/08/python-20151208/
#sys.setrecursionlimit(5000)


if six.PY2 and sys.getdefaultencoding()=='ascii':
    import imp
    imp.reload(sys)
    sys.setdefaultencoding('utf-8')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.join(os.path.realpath(os.path.dirname(__file__)), os.pardir)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2dx3sbj0#=4k$xu=8h52to&a2zia%%lr(w2h4wf$zb(ux6v9az'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']
# 生产环境不开启跨域False https://zhuanlan.zhihu.com/p/25080236
CORS_ORIGIN_ALLOW_ALL = False # 开发环境配置True

# 用CORS 解决vue.js django跨域调用 https://www.jianshu.com/p/1fd744512d83
# 配置允许跨域访问的域名
# CORS_ORIGIN_ALLOW_ALL = False
# 默认值是全部:
CORS_ORIGIN_WHITELIST = (
)
# 或者定义允许的匹配路径正则表达式. CORS_ORIGIN_REGEX_WHITELIST = ('^(https?://)?(\w+.)?>google.com$', )
CORS_ORIGIN_REGEX_WHITELIST = (r'^(https?://)?(\w+\.)?lqdzj\.cn$', )

ADMINS = (
    ('admin', '17074810135m0@sina.cn'),
)
MANAGERS = ADMINS

# Application definition

INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'jwt_auth',
    'xadmin',
    'crispy_forms',
    'reversion',

    'django_extensions',
    'corsheaders',
    'rect',
    'storages',
    #'sutra',
    'xapps',


    'django_celery_beat',
    'django_celery_results',
    'celery',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cutrect.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_ROOT, "templates"),
            os.path.join(PROJECT_ROOT, "xapps/common/templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
        },
    },
]

WSGI_APPLICATION = 'cutrect.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cutrect_prod',
        'USER': 'lqzj',
        'PASSWORD': 'lqdzjsql',
        'HOST': '127.0.0.1',
        'PORT': '5432',

    },
    # 'sutra_db': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'sutra.sqlite3'),
    # }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated', ),
    "DEFAULT_PAGINATION_CLASS": "api.pagination.StandardPagination",
    'PAGE_SIZE': 20,
    'DEFAULT_AUTHENTICATION_CLASSES': (
    'jwt_auth.authentication.JWTAuthentication',
    'rest_framework.authentication.SessionAuthentication',
    )

}

JWT_AUTH = {
    'JWT_RESPONSE_PAYLOAD_HANDLER':
        'jwt_auth.serializers.jwt_response_payload_handler',
    'JWT_PAYLOAD_HANDLER': 'jwt_auth.serializers.jwt_payload_handler',
}

CORS_ORIGIN_WHITELIST = (
    'lqdzj.cn',
    'localhost:8080',
    '127.0.0.1:8000'
)

CORS_ORIGIN_REGEX_WHITELIST = (r'^(https?://)?(\w+\.)?lqdzj\.cn$', )

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'logfile': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': os.path.join("/opt/django/logs/cutrect", "standard.log"),
                'maxBytes': 50000,
                'backupCount': 2,
                'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        # 'django.db.backends': {
        #     'handlers': ['console'],
        #     'level': 'DEBUG',
        # }
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'  # 'UTC'

DATE_FORMAT = 'Y-m-d'
DATETIME_FORMAT = 'Y-m-d H:i'
TIME_FORMAT = 'H:i'
# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-Hans'  # 'en-us'

LANGUAGES = (
    ('en', _('English')),
    ('zh-hans', _('Chinese')),
)

SITE_ID = 1

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/www/cutrect/media'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
# 当运行 python manage.py collectstatic 的时候
# STATIC_ROOT 文件夹 是用来将所有 STATICFILES_DIRS 中所有文件夹中的文件，以及各 app 中 static 中的文件都复制过来
# 把这些文件放到一起是为了用 apache/nginx 等部署的时候更方便
STATIC_ROOT = '/www/cutrect/static'

# Additional locations of static files
# STATICFILES_DIRS = (
#     # Put strings here, like "/home/html/static" or "C:/www/django/static".
#     # Always use forward slashes, even on Windows.
#     # Don't forget to use absolute paths, not relative paths.
# )
# Add for vuejs

STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'xapps/common/static'),
]

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

XADMIN_TITLE = _(u"龙泉大藏经切分平台")
XADMIN_FOOTER_TITLE = _(u"北京 龙泉寺-AIITC.inc")

# Redis Cache Settings
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    },
}

# DEFAULT SESSION ENGINE IS 'django.contrib.sessions.backends.db'
# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_CACHE_ALIAS = "default"
# Redis Cache Settings end


#使用 supervisor 管理进程
#http://liyangliang.me/posts/2015/06/using-supervisor/
#Celery Tasks 参数介绍.
#http://www.jianshu.com/p/d8cbd4c72758


DATABASE_ROUTERS = ['cutrect.db_router.DBRouter']

# 定制celery任务，使用AWS的SQS服务
CELERY_TIMEZONE = 'UTC'
CELERY_ENABLE_UTC = True

CELERY_BROKER_USER = os.environ.get('AWS_ACCESS_KEY', '')
CELERY_BROKER_PASSWORD = os.environ.get('AWS_SECRET_KEY', '')

CELERY_BROKER_TRANSPORT = 'sqs'
CELERY_BROKER_TRANSPORT_OPTIONS = {
    'polling_interval': 3,
    'region': 'cn-north-1',
    'visibility_timeout': 3600,
    'queue_name_prefix': 'lq-prod-'
}

CELERY_WORKER_STATE_DB = '/var/run/celery/worker.db'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
CELERY_WORKER_PREFETCH_MULTIPLIER = 0         # See https://github.com/celery/celery/issues/3712
#CELERY_RESULT_BACKEND = 'sqla+sqlite:///results.sqlite'
CELERY_RESULT_BACKEND = 'db+sqlite:///results.sqlite'
CELERY_DEFAULT_QUEUE = 'lqcharacter_sqs'
CELERY_QUEUES = {
    CELERY_DEFAULT_QUEUE: {
        'exchange': CELERY_DEFAULT_QUEUE,
        'binding_key': CELERY_DEFAULT_QUEUE,
    }
}

CELERY_BROKER_CONNECTION_RETRY=False

CELERY_IMPORTS = (
        'cutrect.celery_tasks',
    )

## 系统邮箱设置
EMAIL_HOST = 'smtp.sina.cn'
EMAIL_PORT = 25
EMAIL_HOST_USER = '17074810135m0@sina.cn'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PW', '')
EMAIL_USE_TLS = True
EMAIL_FROM = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
