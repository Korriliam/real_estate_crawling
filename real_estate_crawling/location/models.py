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

    class Meta:
        app_label = 'location'
        # db_table = "Statistic"

class Offer(models.Model):
    '''

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
    last_change = models.DateTimeField(null=True, blank=True)

class UserAgent(models.Model):
    '''
    Contains a list of user agents
    '''
    user_agent_string = models.CharField(max_length=500)
