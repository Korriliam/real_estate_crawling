from __future__ import unicode_literals
# -*- coding: utf-8 -*-
import scrapy


class Seloger1Spider(scrapy.Spider):
    name = "seloger1"
    start_urls = [
        'http://www.seloger.com/recherche.htm?org=engine&idtt=1&nb_pieces=&pxmax=800&idtypebien=2%2C1&ci=750113%2C750105#idtt=1&idtypebien=1&idtypebien=2&&pxmax=800&&surfacemin=20&&ci=750105,750113&'
    ]

    def parse(self, response):
        results = response.xpath('//section[@class="liste_resultat"]/article')
        links = results.xpath("//div[@class='list-lbc']/a/@href").extract()
        titles = results.xpath('//div[@class="listing_infos"]/h2/text()').extract()
        prix = results.xpath('//div[@class="price "]/a/text()').extract()
        lieux = results.xpath('//div[@class="listing_infos"]/h2/a/span/text()').extract()
        # date = results.xpath('//div[@class="date"]/text()').extract()
        # surface = results.xpath('//div[@class="placement"]/text()').extract()
        for i,elmt in enumerate(titles):
            print elmt #name
            print prix[i] # price
            print links[i]
            print date[i]
            print lieux[i]
            #surface
