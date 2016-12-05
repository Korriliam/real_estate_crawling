from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from scrapy.http.request import Request
from location.models import Offer
from datetime import datetime
import urlparse
import scrapy
import traceback

class Seloger1Spider(scrapy.Spider):
    name = "seloger1"
    surface_min = 20
    prix_max = 800
    start_urls = [
        'http://www.seloger.com/list.htm?cp=75&idtt=1&idtypebien=1&pxmin=&pxmax={0}&surfacemin={1}&surfacemax=&LISTING-LISTpg=1'.format(prix_max,surface_min)
    ]

    def __init__(self, *args, **kwargs):
        pass

    def parse(self, response):
        yield Request(response.url, self.parse_next_page, dont_filter=True)

    def parse_next_page(self,response):
        try:
            page_suiv = response.xpath('.//div[@class="page_number"]/a[position()=1]/@href').extract()[0]
            for elmt in response.xpath('.//section[@class="liste_resultat"]/article[@id]'):
                html_id = elmt.xpath(".//@id").extract()[0]
                offer = Offer.objects.filter(html_id=html_id).distinct()
                if not Offer.objects.filter(html_id=html_id).count():
                    offer = Offer()
                else:
                    offer = offer[0]
                offer.html_id = html_id
                offer.url = elmt.xpath(".//div/h2/a/@href").extract()[0]
                offer.price = elmt.xpath('.//a[@class="amount"]/text()').extract()[0][:-3]
                offer.address = elmt.xpath('.//div[@class="listing_infos"]/h2/a/span/text()').extract()[0]
                # agence = elmt.xpath('//div[@class="agency_contact"]/p[@class="agency_name"]/span/text()').extract()
                # phone = elmt.xpath('//div[@class="agency_contact"]/div/@data-phone').extract()
                offer.tax_included = 'CC' in elmt.xpath('.//a[@class="amount"]/sup/text()').extract()[0]
                offer.last_change = datetime.now()
                offer.save()
                yield Request(offer.url,
                          callback=self.parse_one_annonce, meta={'offer':offer})
        except UnboundLocalError:
            print "Crawling ended. Exitting..."
            exit()

        parse = urlparse.urlparse(response.url)
        n = urlparse.parse_qs(parse.query)['LISTING-LISTpg'][0]

        parsed = int(n)
        page_suiv = response.url[:-len(n)] + str(parsed + 1)

        yield Request(page_suiv,
                            callback=self.parse_next_page)

    def parse_one_annonce(self, response):
        surface = response.xpath('//div[@class="criterions"]/ol/li[@class="resume__critere"]/text()').extract()
        descriptionDetaillee = response.xpath('//div[@id="detail"]/p[@class="description"]/text()').extract()
        offer = response.meta['offer']
        offer.surface = surface[1]
        offer.description = descriptionDetaillee[0]
        offer.save()
