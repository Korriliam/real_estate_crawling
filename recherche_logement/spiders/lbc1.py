from __future__ import unicode_literals
# -*- coding: utf-8 -*-
import scrapy


class Lbc1Spider(scrapy.Spider):
    name = "seloger1"
    start_urls = (
        'http://www.leboncoin.fr/locations/offres/ile_de_france/paris/?f=a&th=1&mre=800&sqs=1&ret=2&location=Paris%2075013%2CParis%2075005',
    )

    def parse(self, response):
        results = response.xpath('//div[@class="list-lbc"]/a/div[@class="lbc"]')
        links = results.xpath("//div[@class='list-lbc']/a/@href").extract()
        titles = results.xpath('//div[@class="detail"]/div[@class="title"]/text()').extract()
        prix = results.xpath('//div[@class="price"]/text()').extract()
        lieux = results.xpath('//div[@class="placement"]/text()').extract()
        date = results.xpath('//div[@class="date"]/text()').extract()
        for i,elmt in enumerate(titles):
            print elmt #name
            print prix[i] # price
            print links[i]
            print date[i]
            print lieux[i]
            #surface



