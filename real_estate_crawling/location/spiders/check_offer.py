from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from location.models import Offer
from scrapy.spiders import CrawlSpider
from util.database import check_connection
from MySQLdb import OperationalError
import logging
import re

log = logging.getLogger(__name__)

class CheckOffer(CrawlSpider):
    name = "check_offer"
    handle_httpstatus_list = [200, 301, 404, 500]

    def __init__(self):
        super(self.__class__, self).__init__()
        urls = Offer.objects.values('url').filter(active=True)

        self.start_urls = set([url['url'] for url in urls])
        self.custom_settings = {
            'HTTPCACHE_ENABLED': False,
            'RETRY_ENABLED': False
        }


    def parse(self, response):
        check_connection()
        if response.status in (404, 500):
            self.toggle_disable(response)
        elif 'redirect_urls' in response.request.meta:
            if not re.match('.*-g439-\d{2}-r\d+$', response.url) and 'pap.fr' in response.url:
                log.info('PAPTOGG')
                self.toggle_disable(response)
            if not re.match('.*\d+\.htm\\?.*', response.url):
                log.info('SELOGERTOGG')
                self.toggle_disable(response)

    def toggle_disable(self, response):
        log.info('Toggling offer to disabled')
        log.info('url %s unfound' % response.request.meta)
        obj = Offer.objects.filter(url=response.request.meta['redirect_urls'][0])[0] if 'redirect_urls' in response.request.meta else \
            Offer.objects.filter(url=response.url)[0]
        obj.active = False
        obj.save()
