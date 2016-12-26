from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from location.models import Offer
from scrapy.spiders import CrawlSpider
import logging

log = logging.getLogger(__name__)

class CheckOffer(CrawlSpider):
    name = "check_offer"
    handle_httpstatus_list = [404]

    def __init__(self):
        super(self.__class__, self).__init__()
        urls = Offer.objects.values('url').filter(active=True)

        self.start_urls = set([url['url'] for url in urls])
        self.custom_settings = {'HTTPCACHE_ENABLED': False}

    def parse(self, response):
        if response.status == 404:
            log.info('Toggling offer to disabled')
            log.info('url %s unfound' % response.request.meta['request_urls'])
            obj = Offer.objects.filter(url=response.request.meta['request_urls'])[0]
            obj.active = False
            obj.save()
