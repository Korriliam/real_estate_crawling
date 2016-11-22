# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.contrib.djangoitem import DjangoItem
from models import Annonces
from scrapy_djangoitem import DjangoItem

class RechercheLogementItem(DjangoItem):
    django_model = Annonces

