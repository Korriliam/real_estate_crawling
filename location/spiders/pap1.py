
from __future__ import unicode_literals
# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.request import Request
from recherche_logement.location.models import Annonces
import urlparse
from datetime import datetime
import traceback

class Lbc1Spider(scrapy.Spider):
    name = "lbc1"
    start_urls = (
        'http://www.leboncoin.fr/locations/offres/ile_de_france/paris/?f=a&th=1&mre={0}&sqs=1&ret=2'.format(800),
    )


    def parse(self, response):
        results = response.xpath('//div[@class="list-lbc"]')
        for i,elmt in enumerate(results):
            htmlId = elmt.xpath("//div[@class='content-color']/div[@class='list-lbc']/a[@title]/@href").extract()
            htmlId = [oo.replace("http://www.leboncoin.fr/locations/","").replace(".htm?ca=12_s","") for oo in htmlId]
            links = elmt.xpath("//div[@class='list-lbc']/a/@href").extract()
            # descriptions = elmt.xpath('//div[@class="listing_infos"]/p/text()').extract()
            titles = elmt.xpath('//div[@class="detail"]/div[@class="title"]/text()').extract()
            prix = elmt.xpath('//div[@class="price"]/text()').extract()
            prix = [oo.replace(" ","").replace("\n","") for oo in prix]
            lieux = elmt.xpath('//div[@class="placement"]/text()').extract()
            lieux = [oo.replace('\n','').replace('  ','') for oo in lieux]


            break
        page_suiv = elmt.xpath('//ul[@id="paging"]/li/a/@href').extract()[0]
        for i in range(len(prix)):
            ann = Annonces.objects.filter(htmlId=htmlId[i]).distinct()
            if Annonces.objects.filter(htmlId=htmlId[i]).count() == 0:
                object = Annonces()
            else:
                object = ann[0]
            object.prix = prix[i][:-1]
            # object.agence = agence[i]
            # object.description = descriptions[i]
            object.title = titles[i]
            # object.phone = phone[i]
            # object.chargesComprises = (cc[i] in "CC")
            object.lieux = lieux[i]
            object.url = links[i]
            object.htmlId = htmlId[i]
            object.lastChange = datetime.now()
            object.save()
            yield Request(links[i], callback=self.parse_one_annonce, meta={'object':object})

        yield Request(response.url+"&o=2",
                              callback=self.parse_following_page)



    def parse_following_page(self,response):
        results = response.xpath('//div[@class="list-lbc"]')
        for i,elmt in enumerate(results):
            htmlId = elmt.xpath("//div[@class='content-color']/div[@class='list-lbc']/a[@title]/@href").extract()
            htmlId = [oo.replace("http://www.leboncoin.fr/locations/","").replace(".htm?ca=12_s","") for oo in htmlId]
            links = elmt.xpath("//div[@class='list-lbc']/a/@href").extract()
            # descriptions = elmt.xpath('//div[@class="listing_infos"]/p/text()').extract()
            titles = elmt.xpath('//div[@class="detail"]/div[@class="title"]/text()').extract()
            prix = elmt.xpath('//div[@class="price"]/text()').extract()
            prix = [oo.replace(" ","").replace("\n","") for oo in prix]
            lieux = elmt.xpath('//div[@class="placement"]/text()').extract()
            lieux = [oo.replace('\n','').replace('  ','') for oo in lieux]
            break
        try:
            for i in range(len(prix)):
                ann = Annonces.objects.filter(htmlId=htmlId[i]).distinct()
                if Annonces.objects.filter(htmlId=htmlId[i]).count() == 0:
                    object = Annonces()
                else:
                    object = ann[0]
                object.prix = prix[i][:-1]
                # object.agence = agence[i]
                # object.description = descriptions[i]
                object.title = titles[i]
                # object.phone = phone[i]
                # object.chargesComprises = (cc[i] in "CC")
                object.lieux = lieux[i]
                object.url = links[i]
                object.htmlId = htmlId[i]
                object.lastChange = datetime.now()
                object.save()
                yield Request(links[i], callback=self.parse_one_annonce, meta={'object':object})

        except UnboundLocalError:
            print "Crawling terminé. Exitting..."
            exit()
        parse = urlparse.urlparse(response.url)
        try:
            n = urlparse.parse_qs(parse.query)['o'][0]
        except KeyError:
            print traceback.format_exc()
            print parse
            print response.url
            exit()

        parsed = int(n)
        page_suiv = response.url[:-len(n)] + str(parsed + 1)

        yield Request(page_suiv,
                              callback=self.parse_following_page)


    def parse_one_annonce(self, response):
        surface = response.xpath('//th[text()="Surface : "]/following::td[1]/text()').extract()
        descriptionDetaillee = response.xpath('///div[@class="AdviewContent"]/div[@class="content"]/text()').extract()
        # phone = response.xpath("//div[@class='lbc_links']/span[@class='lbcPhone']/span[@id='phoneNumber']/a/@href").extract()[53:-1]
        print(surface)
        print(descriptionDetaillee)
        # print(phone)
        obj = response.meta['object']
        obj.surface = surface[0]
        obj.description = descriptionDetaillee[0]
        obj.save()
