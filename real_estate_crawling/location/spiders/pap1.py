
from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from scrapy.http.request import Request
from location.models import Offer
from datetime import datetime
import scrapy
import urlparse
import traceback
import re

class pap1Spider(scrapy.Spider):
    name = "pap1"
    start_urls = (
        'http://www.pap.fr/annonce/locations-appartement-paris-75-g439-jusqu-a-{0}-euros-a-partir-de-20-m2'.format(800),
    )


    def parse(self, response):
        yield Request(response.url, self.parse_next_page, dont_filter=True)


    def parse_next_page(self,response):
        try:
            for i in response.xpath('.//div[@class="box search-results-item"]'):
                html_id = eval(results[0].xpath('.//a[@data-annonce]/@data-annonce').extract()[0].replace('false','False').replace('true','True'))
                offer = Offer.objects.filter(html_id=html_id).distinct()
                if Offer.objects.filter(html_id=html_id).count() == 0:
                    offer = Offer()
                else:
                    offer = offer[0]

                offer.url = 'http://www.pap.fr' + elmt.xpath(".//div[@class='float-right']/a/@href").extract()[0]
                offer.title = elmt.xpath('.//span[@class="h1"]/text()').extract()[0]
                offer.price = elmt.xpath('.//span[@class="price"]/strong/text()').extract()[0][:-2]
                offer.address = elmt.xpath('.//p[@class="item-description"]/strong/text()').extract()[0]
                yield Request(offer.url, callback=self.parse_one_annonce, meta={'object':offer})

        except UnboundLocalError:
            print "Crawling ended. Exitting..."
            exit()

        if re.match('.*-\d+$',response.url):
            page_suiv = response.url[:-len(n)] + str(parsed + 1)
        else:
            page_suiv = response.url + '-2'

        yield Request(page_suiv,
                              callback=self.parse_next_page)


    def parse_one_annonce(self, response):
        surface = response.xpath('//li[text()="Surface : "]/following::td[1]/strong/text()').extract()
        descriptionDetaillee = response.xpath('///div[@class="AdviewContent"]/div[@class="content"]/text()').extract()
        # phone = response.xpath("//div[@class='lbc_links']/span[@class='lbcPhone']/span[@id='phoneNumber']/a/@href").extract()[53:-1]
        print(surface)
        print(descriptionDetaillee)
        # print(phone)
        obj = response.meta['object']
        obj.surface = surface[0]
        obj.description = descriptionDetaillee[0]
        obj.save()
