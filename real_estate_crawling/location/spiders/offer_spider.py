from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from scrapy.http.request import Request
from scrapy.spiders import CrawlSpider

class offerSpider(CrawlSpider):
    def __init__(self, max_price=None, min_price=None, max_area=None, min_area=None):
        self.max_price = max_price if max_price else ''
        self.min_price = min_price if min_price else ''
        self.max_area = max_area if max_area else ''
        self.min_area = min_area if min_area else ''

    def parse(self, response):
        yield Request(response.url, self.parse_next_page, dont_filter=True)

    def parse_next_page(self, response):
        pass

    def parse_one_annonce(self, response):
        offer = response.meta['object']
        if response.url != offer.url:
            offer.url = response.url
        return offer
