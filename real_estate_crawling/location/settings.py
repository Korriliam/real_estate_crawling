from __future__ import unicode_literals
# -*- coding: utf8 -*-

SECRET_KEY = "secret key value"

ALLOWED_HOSTS = ['localhost','127.0.0.1']

DOWNLOAD_DELAY = 7.0

RANDOMIZE_DOWNLOAD_DELAY = 2.5

# une option de scrapy, fait varier le temps entre deux requetes successives dans un temps compris entre 10 et 39.0
# AUTOTHROTTLE_ENABLED = True
# AUTOTHROTTLE_START_DELAY = 5.0
# AUTOTHROTTLE_MAX_DELAY = 19.5
# AUTOTHROTTLE_DEBUG = True # pour activer l'affichage de statistiques supplémentaires

# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

ALLOWED_HOSTS = ['korriliam.pythonanywhere.com',]

CONCURRENT_REQUESTS = 1 # nombre de requetes vers un site en même temps (128 au maximum) signifie que l'on recupere 1
                        # site à la fois.
BOT_NAME = 'real_estate_crawling.location'

SPIDER_MODULES = ['real_estate_crawling.location.spiders']
NEWSPIDER_MODULE = 'real_estate_crawling.location.spiders'

DOWNLOADER_MIDDLEWARES = {
        # 'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
        'util.user_agent_rotator.RotateUserAgent': 1,
}

DEBUG = False

#Nombre de redirection successives que l'on peut effectuer.
REDIRECT_MAX_TIMES = 3

DOWNLOAD_TIMEOUT = 180

EXTENSIONS = {
    'scrapy.contrib.corestats.CoreStats': 500,
    'scrapy.contrib.logstats.LogStats': 500,
    'util.statsToDb.statsToDb': 800,
    # 'util.EndMiddleware.VacuumJobdir':900
}

HTTPCACHE_ENABLED = False

RETRY_ENABLED = True # Booléen qui dit si oui on non, si je n'arrive pas à acceder à une page, je réeessaye (non ici)
                        # Si c'était vrai, on ressayerai à l'infini

ROBOTSTXT_OBEY = False# Our bot don't follow robots.txt recommandations. On ne suis pas les recommandations des robots.Txt.

ROOT_URLCONF = 'location.urls'


#STATIC_URL = '/static/'

RETRY_HTTP_CODES = [500, 502, 503, 504, 408]

INSTALLED_APPS=(
    # 'real_estate_crawling.location',
    'location',
    'django.contrib.admin',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.staticfiles',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ]
        }
    },
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# To configure Django en général, et en particuleir la connexion à la base de données.
DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'korriliam$location',
        'USER': 'korriliam',
        'PASSWORD': 'location',
        'HOST': 'korriliam.mysql.pythonanywhere-services.com',
        'CONN_MAX_AGE': 299,
    }
}



STATIC_URL = '/static/'
STATIC_ROOT = '/home/korriliam/real_estate_crawling/real_estate_crawling/static/'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

