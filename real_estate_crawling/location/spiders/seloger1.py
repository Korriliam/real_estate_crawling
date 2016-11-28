from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from urlparse import urlparse
import scrapy
from scrapy.http.request import Request
from location.models import Offer
import urlparse
from datetime import datetime
import traceback

class Seloger1Spider(scrapy.Spider):
    name = "seloger1"
    surface_min = 20
    prix_max = 800
    start_urls = [
        # 'http://www.seloger.com/recherche.htm?org=engine&idtt=1&nb_pieces=&pxmax={0}&idtypebien=2%2C1&ci=750113%2C750105#idtt=1&idtypebien=1&idtypebien=2&&pxmax=800&&surfacemin={1}&&ci=750105,750113&'.format(prix_max,surface_min)
        'http://www.seloger.com/recherche.htm?cp=75&org=advanced_search&idtt=1&refannonce=&pxmin=&pxmax={0}&surfacemin={1}&surfacemax=&idtypebien=1&surf_terrainmin=&surf_terrainmax=&etagemin=&etagemax=&idtypechauffage=&idtypecuisine='.format(prix_max,surface_min)


    ]

    def parse(self, response):
        results = response.xpath('//section[@class="liste_resultat"]/article[@id]')
        for i,elmt in enumerate(results):
            htmlId = elmt.xpath("//article/@id").extract()
            links = elmt.xpath("//div/h2/a/@href").extract()
            descriptions = elmt.xpath('//div[@class="listing_infos"]/p/text()').extract()
            titles = elmt.xpath('//div[@class="listing_infos"]/h2/a/text()').extract()
            prix = elmt.xpath('//div[@class="amount"]/a/text()').extract()
            lieux = elmt.xpath('//div[@class="listing_infos"]/h2/a/span/text()').extract()
            # date = elmt.xpath('//div[@class="date"]/text()').extract()
            # agence = elmt.xpath('//div[@class="agency_contact"]/p[@class="agency_name"]/span/text()').extract()
            # phone = elmt.xpath('//div[@class="agency_contact"]/div/@data-phone').extract()
            page_suiv = elmt.xpath('//div[@class="page_number"]/a[position()=1]/@href').extract()[0]
            cc = elmt.xpath('//div[@class="amount"]/a/sup/text()').extract()
            break

        for i in range(len(prix)):
            ann = Annonces.objects.filter(htmlId=htmlId[i]).distinct()
            if Annonces.objects.filter(htmlId=htmlId[i]).count() == 0:
                object = Annonces()
            else:
                object = ann[0]
            object.prix = prix[i][:-2]
            # object.agence = agence[i]
            object.description = descriptions[i]
            object.title = titles[i]
            object.phone = phone[i]
            object.chargesComprises = (cc[i] in "CC")
            object.lieux = lieux[i]
            object.url = links[i]
            object.htmlId = htmlId[i]
            object.lastChange = datetime.now()
            object.save()
            yield Request(links[i],
                              callback=self.parse_one_annonce, meta={'object':object})

        yield Request(page_suiv,
                              callback=self.parse_following_page)



    def parse_following_page(self,response):
        results = response.xpath('//section[@class="liste_resultat"]/article[@id]')
        for i,elmt in enumerate(results):
            htmlId = elmt.xpath("//article/@id").extract()
            links = elmt.xpath("//div/h2/a/@href").extract()
            descriptions = elmt.xpath('//div[@class="listing_infos"]/p/text()').extract()
            titles = elmt.xpath('//div[@class="listing_infos"]/h2/a/text()').extract()
            prix = elmt.xpath('//div[@class="amount"]/a/text()').extract()
            lieux = elmt.xpath('//div[@class="listing_infos"]/h2/a/span/text()').extract()
            # date = elmt.xpath('//div[@class="date"]/text()').extract()
            # agence = elmt.xpath('//div[@class="agency_contact"]/p[@class="agency_name"]/span/text()').extract()
            # phone = elmt.xpath('//div[@class="agency_contact"]/div/@data-phone').extract()
            page_suiv = elmt.xpath('//div[@class="page_number"]/a[position()=1]/@href').extract()[0]
            cc = elmt.xpath('//div[@class="amount"]/a/sup/text()').extract()
            break

        try:
            for i in range(len(prix)):
                ann = Annonces.objects.filter(htmlId=htmlId).distinct()
                if Annonces.objects.filter(htmlId=htmlId).count() == 0:
                    object = Annonces()
                else:
                    object = ann[0]
                object.prix = prix[i][:-2]
                object.agence = agence[i]
                object.description = descriptions[i]
                object.title = titles[i]
                object.phone = phone[i]
                object.chargesComprises = (cc[i] in "CC")
                object.lieux = lieux[i]
                object.url = links[i]
                object.htmlId = htmlId[i]
                object.lastChange = datetime.now()
                object.save()
                yield Request(links[i],
                          callback=self.parse_one_annonce, meta={'object':object})
        except UnboundLocalError:
            print "Crawling terminé. Exitting..."
            exit()
            parse = urlparse.urlparse(response.url)
        try:
            n = urlparse.parse_qs(parse.query)['LISTING-LISTpg'][0]
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
        surface = response.xpath('//div[@class="criterions"]/ol/li[@class="resume__critere"]/text()').extract()
        descriptionDetaillee = response.xpath('//div[@id="detail"]/p[@class="description"]/text()').extract()
        print(surface)
        print(descriptionDetaillee)
        obj = response.meta['object']
        obj.surface = surface[1]
        obj.description = descriptionDetaillee[0]
        obj.save()
