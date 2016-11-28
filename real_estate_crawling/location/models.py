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

    # class Meta:
        # db_table = "Statistic"

class Offer(models.Model):
    '''

    '''
    prix = models.BigIntegerField(null=True,blank=True)
    url = models.URLField()
    title = models.CharField(max_length=120,null=True,blank=True)
    surface = models.CharField(max_length=120,null=True,blank=True)
    description = models.CharField(max_length=1000,null=True,blank=True)
    agence = models.CharField(max_length=100,null=True,blank=True)
    chargesComprises = models.NullBooleanField(null=True,blank=True)
    lieux = models.CharField(max_length=200,null=True,blank=True)
    phone = models.CharField(max_length=100,null=True,blank=True)
    htmlId = models.CharField(max_length=100,null=True,blank=True)
    lastChange = models.DateTimeField(null=True, blank=True)
    # class Meta:
        # db_table = "Offer"

class UserAgent(models.Model):
    '''
    Contains a list of user agents
    '''
    user_agent_string = models.CharField(max_length=500)

    # class Meta:
        # db_table = "UserAgent"
