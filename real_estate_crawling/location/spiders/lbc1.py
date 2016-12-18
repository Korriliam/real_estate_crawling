from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from scrapy.http.request import Request
from location.models import Offer, Source, OfferCategory
import urlparse
from datetime import datetime
from location.spiders.offer_spider import offerSpider

class Lbc1Spider(offerSpider):
    name = "lbc1"
    max_price = 800
    start_urls = (
        'http://www.leboncoin.fr/locations/offres/ile_de_france/paris/?f=a&th=1&mre=&sqs=1&ret=2',#.format(max_price),
    )

    offer_category_id = OfferCategory.objects.filter(name='location')[0].id
    source_id = Source.objects.filter(name='leboncoin')[0].id

    def parse_next_page(self, response):
        try:
            for elmt in response.xpath('.//li[@itemtype="http://schema.org/Offer"]'):
                html_id = elmt.xpath('.//div[@class="saveAd"]/@data-savead-id').extract()[0]
                check_offer = Offer.objects.filter(html_id=html_id).distinct()
                if Offer.objects.filter(html_id=html_id).count() == 0:
                    offer = Offer()
                else:
                    offer = check_offer[0]

                offer.html_id = html_id
                offer.source_id = self.source_id
                offer.offer_category_id = self.offer_category_id
                offer.url = elmt.xpath('.//a/@href').extract()[0]
                offer.title = elmt.xpath('.//section[@class="item_infos"]/h3/text()').extract()[0].strip()
                try:
                    offer.price = elmt.xpath('.//div[@class="price"]/text()').extract()[0].strip()
                except:
                    offer.price = None
                offer.address = elmt.xpath('.//p[@itemtype="http://schema.org/Place"]/text()').extract()[0].strip()
                offer.last_change = datetime.now()
                offer.save()
                yield Request('http:' + offer.url, callback=self.parse_one_annonce, meta={'object':offer})
        except UnboundLocalError:
            print "Crawling done. Exiting..."
            exit()
        parse = urlparse.urlparse(response.url)
        t = True

        try:
            n = urlparse.parse_qs(parse.query)['o'][0]
        except KeyError:
            t = False
            next_page = response.url + '&o=2'
            yield Request(next_page,
                                callback=self.parse_next_page)

        if t:
            parsed = int(n)
            next_page = response.url[:-len(n)] + str(parsed + 1)

            yield Request(next_page,
                                callback=self.parse_next_page)


    def parse_one_annonce(self, response):
        try:
            surface = response.xpath('//span[text()="Surface"]/following::text()').extract()
        except:
            pass
        descriptionDetaillee = response.xpath('//div/p[@itemprop="description"]/text()').extract()
        offer = response.meta['object']
        try:
            offer.area = surface[0]
        except:
            pass
        offer.description = descriptionDetaillee[0]
        offer.save()
