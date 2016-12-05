from __future__ import unicode_literals
# -*- coding: utf8 -*-
#sys.path.append("/home/korrigan/real_estate_crawling/real_estate_crawling/location")

# os.environ["SECRET_KEY"] = "secret key value"
# import django
# django.setup()

SECRET_KEY = "secret key value"

ALLOWED_HOSTS = ['localhost','127.0.0.1']

DOWNLOAD_DELAY = 4.0

# une option de scrapy, fait varier le temps entre deux requetes successives dans un temps compris entre 10 et 39.0
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5.0
AUTOTHROTTLE_MAX_DELAY = 39.0
AUTOTHROTTLE_DEBUG = True # pour activer l'affichage de statistiques supplémentaires

AUTOTHROTTLE_TARGET_CONCURRENCY = 2


CONCURRENT_REQUESTS_PER_DOMAIN = 2 # nombre de requetes vers un site en même temps (128 au maximum) signifie que l'on recupere 1
                        # site à la fois.
BOT_NAME = 'real_estate_crawling.location'

SPIDER_MODULES = ['real_estate_crawling.location.spiders']
NEWSPIDER_MODULE = 'real_estate_crawling.location.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'location (+http://www.yourdomain.com)'

# les classes qui vont traiter les requetes et reponse avant/apres téléchargement
# unepriorité est attribuée à chaque downloader middleware
DOWNLOADER_MIDDLEWARES = {
        'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
        #activation de rotateUserAgents ici. Va attributer user agent different à chaque requête.
}

DEBUG = True

#Nombre de redirection successives que l'on peut effectuer.
REDIRECT_MAX_TIMES = 3

DOWNLOAD_TIMEOUT = 180

EXTENSIONS = {
    'scrapy.contrib.corestats.CoreStats': 500,
    'scrapy.contrib.logstats.LogStats': 500,
    'util.statsToDb.statsToDb': 800,
    'scrapy.contrib.throttle.AutoThrottle': 900,
    # 'util.EndMiddleware.VacuumJobdir':900
}

RETRY_ENABLED = False # Booléen qui dit si oui on non, si je n'arrive pas à acceder à une page, je réeessaye (non ici)
                        # Si c'était vrai, on ressayerai à l'infini

ROBOTSTXT_OBEY = False # Our bot don't follow robots.txt recommandations. On ne suis pas les recommandations des robots.Txt.

ROOT_URLCONF = 'location.urls'

DATABASE_SCHEMA = 'location'

STATIC_URL = '/static/'


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
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DATABASE_SCHEMA,
        'USER': 'location',
        'PASSWORD': 'location',
        'HOST': 'localhost',
        }
}

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

