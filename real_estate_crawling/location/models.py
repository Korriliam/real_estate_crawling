from __future__ import unicode_literals
# -*- coding: utf8 -*-

from django.db import models



class Statistic(models.Model):
    '''
    Contains the stats attached to each crawling operation/session (nb of results, ...)
    '''
    startTime = models.DateTimeField()
    finishTime = models.DateTimeField()
    finishReason = models.CharField(max_length=200)
    requestBytes = models.BigIntegerField()
    responseBytes = models.BigIntegerField()
    requestCount = models.BigIntegerField()
    responseCount = models.BigIntegerField()
    responseReceivedCount = models.BigIntegerField()
    requestDepthMax = models.IntegerField()
    requestStatusCount200 = models.BigIntegerField()
    requestStatusCount301 = models.BigIntegerField()
    requestStatusCount302 = models.BigIntegerField()
    requestStatusCount500 = models.BigIntegerField()
    requestStatusCount404 = models.BigIntegerField()
    dupeFiltered = models.BigIntegerField()
    imgCount = models.BigIntegerField()
    nbScrapedItems = models.BigIntegerField()

class UserAgent(models.Model):
    '''
    Contains a list of user agents
    '''
    user_agent_string = models.CharField(max_length=500)

class Source(models.Model):
    '''
    Website mostly
    '''
    url = models.URLField()
    name = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.name

class OfferCategory(models.Model):
    '''
    Location, colocation...
    '''
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Place(models.Model):
    country = models.CharField(max_length=120, null=True, blank=True)
    street = models.CharField(max_length=1000, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postal_code = models.CharField(max_length=120, null=True, blank=True)
    state = models.CharField(max_length=120, null=True, blank=True)

class Offer(models.Model):
    '''
    Offers
    '''
    price = models.BigIntegerField(null=True,blank=True)
    url = models.URLField()
    title = models.CharField(max_length=120,null=True,blank=True)
    area = models.CharField(max_length=120,null=True,blank=True)
    description = models.CharField(max_length=1000,null=True,blank=True)
    agency = models.CharField(max_length=100,null=True,blank=True)
    tax_included = models.NullBooleanField(null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    phone = models.CharField(max_length=100,null=True,blank=True)
    html_id = models.CharField(max_length=100,null=True,blank=True)
    first_crawl_date = models.DateTimeField(null=True, blank=True)
    last_crawl_date = models.DateTimeField(null=True, blank=True)
    source = models.ForeignKey(Source, null=True, blank=True)
    offer_category = models.ForeignKey(OfferCategory, null=True, blank=True)
    place = models.ForeignKey(Place, null=True, blank=True)
    active = models.BooleanField(default=True)

class SourceCategory(models.Model):
    """
     First thought to carry the whole bunch of leboncoin categories.
     Then I thought it could be interessant for other sources in the future
     Include a category's name, its url, being linked to the right row win source
     table.
    """
    name = models.CharField(max_length=120)
    url = models.URLField()
    source = models.ForeignKey(Source)

    def __str__(self):
        return self.name

