from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from location.models import Offer
from scrapy.spiders import CrawlSpider
import logging

log = logging.getLogger(__name__)

class CheckOffer(CrawlSpider):
    name = "check_offer"
    handle_httpstatus_list = [404, 500]

    def __init__(self):
        super(self.__class__, self).__init__()
        urls = Offer.objects.values('url').filter(active=True)

        self.start_urls = set([url['url'] for url in urls])
        self.custom_settings = {'HTTPCACHE_ENABLED': False}

    def parse(self, response):
        if response.status in (404, 500):
            log.info('Toggling offer to disabled')
            log.info('url %s unfound' % response.request.meta)
            obj = Offer.objects.filter(url=response.request.meta['redirect_urls'][0])[0] if 'redirect_urls' in response.request.meta else \
                Offer.objects.filter(url=response.url)[0]
            obj.active = False
            obj.save()
