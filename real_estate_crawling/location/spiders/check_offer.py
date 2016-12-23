from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from scrapy.http.request import Request
from location.models import Offer, Source, OfferCategory
import urlparse
from datetime import datetime
from location.spiders.offer_spider import offerSpider
from scrapy.spiders import CrawlSpider

class CheckOffer(offerSpider):
    name = "check_offer"

    source_id = Source.objects.filter(name='leboncoin')[0].id


    def __init__(self, category="location"):
        super(self.__class__, self).__init__()
        urls = Offer.objects.values('url').filter(active=True)

        self.start_urls = set([url['url'] for url in urls])
        self.custom_settings = {'HTTPCACHE_ENABLED': False}

