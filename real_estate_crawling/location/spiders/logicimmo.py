from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from scrapy.http.request import Request
from location.models import Offer, Source, OfferCategory
import urlparse
from datetime import datetime
from location.spiders.offer_spider import offerSpider


class LogicimmoSpider(offerSpider):
    name = "logicimmo"
    start_urls = ['http://www.logic-immo.com/location-immobilier-paris-75,100_1/options/groupprptypesids=1,2,6,7,12,15']


    offer_category_id = OfferCategory.objects.filter(name='location')[0].id
    source_id = Source.objects.filter(name=name)[0].id

    def parse_next_page(self, response):
        try:
            for elmt in response.xpath('.//div[@class="offer"]'):
                html_id = elmt.xpath('.//div[@class="mea-async-block"]/div/div[@id]/@id').extract()[0]
                check_offer = Offer.objects.filter(html_id=html_id).distinct()
                if Offer.objects.filter(html_id=html_id).count() == 0:
                    offer = Offer()
                else:
                    offer = check_offer[0]

                offer.html_id = html_id
                offer.source_id = self.source_id
                offer.offer_category_id = self.offer_category_id
                offer.url = elmt.xpath('.//a[@class="offer-link"]/@href').extract()[0]
                # offer.title = elmt.xpath('.//section[@class="item_infos"]/h3/text()').extract()[0].strip()
                try:
                    offer.price = elmt.xpath('.//p[@class="offer-price"]/span/text()').extract()[0].strip()
                except:
                    offer.price = None
                offer.address = elmt.xpath('.//a[@class="offer-block offer-link"]/@title').extract()[0].strip()
                offer.last_change = datetime.now()
                offer.save()
                yield Request(offer.url, callback=self.parse_one_annonce, meta={'object':offer})
        except UnboundLocalError:
            print "Crawling done. Exiting..."
            exit()
        t = True

        try:
            if 'page=' in response.url:
                url = response.url.split('/')
                for i, elmt in enumerate(url):
                    if 'page' in elmt:
                        n = elmt.split('=')[1]
                        url[i] = ''
            else:
                raise
        except:
            t = False
            next_page = response.url + '/page=2'
            yield Request(next_page,
                                callback=self.parse_next_page)

        if t:
            parsed = int(n)
            next_page = '/'.join(url) + 'page=' + str(parsed + 1)

            yield Request(next_page,
                                callback=self.parse_next_page)


    def parse_one_annonce(self, response):
        try:
            surface = response.xpath('//span[@class="offer-area-number"]/text()').extract()
        except:
            pass
        descriptionDetaillee = response.xpath('/div[@class="offer-description-text"]/p/text()').extract()
        offer = response.meta['object']
        try:
            offer.area = surface[0]
        except:
            pass
        offer.description = descriptionDetaillee[0]
        offer.save()
