# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.contrib.djangoitem import DjangoItem
from models import Offer, Statistic, UserAgent
from scrapy_djangoitem import DjangoItem

class OfferItem(DjangoItem):
    django_model = Offer

class StatisticItem(DjangoItem):
    django_model = Statistic

class UserAgentItem(DjangoItem):
    django_model = UserAgent
