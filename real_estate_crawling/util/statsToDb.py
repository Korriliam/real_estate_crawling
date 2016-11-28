from __future__ import unicode_literals
# -*- coding: utf8 -*-

__author__ = 'Guillaume Le Bihan'

from location.models import Statistic
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from django.core.exceptions import MultipleObjectsReturned
from datetime import datetime
import time

class statsToDb(object):
    """
    Sauvegarde de statistiques en base de données à la fermeture du programme.
    """
    def __init__(self):
        """
        Our spider will be called if these signals are sent...
        """
        dispatcher.connect(self.stats_spider_closed, signal=signals.stats_spider_closed)
        dispatcher.connect(self.stats_spider_closed, signal=signals.spider_closed)
        dispatcher.connect(self.stats_spider_closed, signal=signals.engine_stopped)


    def utc2local(self, utc):
        '''
        Convert universal time to local time (gmt + 2 (Paris))
        '''
        epoch = time.mktime(utc.timetuple())
        offset = datetime.fromtimestamp(epoch) - datetime.utcfromtimestamp(epoch)
        return utc + offset

    def stats_spider_closed(self, spider, spider_stats):
        """
        this function is called whenever the spider is done with its work
        """
        item = Statistic()
        # on recupere certaines statistiques qui sont contenues dans un tableau nommé spider_stats.
        item.startTime  = unicode(self.utc2local(spider_stats['start_time']).replace(microsecond=0))
        item.finishTime = unicode(self.utc2local(spider_stats['finish_time']).replace(microsecond=0))
        item.finishReason = spider_stats['finish_reason'].encode('utf-8') if 'finish_reason' in spider_stats else 0
        item.requestBytes = spider_stats['downloader/request_bytes'] if 'downloader/request_bytes' in spider_stats else 0
        item.responseBytes = spider_stats['downloader/response_bytes'] if 'downloader/response_bytes' in spider_stats else 0
        item.requestCount = spider_stats['downloader/request_count'] if 'downloader/request_count' in spider_stats else 0
        item.responseCount = spider_stats['downloader/response_count'] if 'downloader/response_count' in spider_stats else 0
        item.responseReceivedCount = spider_stats['response_received_count'] if 'response_received_count' in spider_stats else 0
        item.requestDepthMax = spider_stats['request_depth_max'] if 'request_depth_max' in spider_stats else 0
        item.requestStatusCount200 = spider_stats['downloader/response_status_count/200'] if 'downloader/response_status_count/200' in spider_stats else 0
        item.requestStatusCount301 = spider_stats['downloader/response_status_count/301'] if 'downloader/response_status_count/301' in spider_stats else 0
        item.requestStatusCount302 = spider_stats['downloader/response_status_count/302'] if 'downloader/response_status_count/302' in spider_stats else 0
        item.requestStatusCount500 = spider_stats['downloader/response_status_count/500'] if 'downloader/response_status_count/500' in spider_stats else 0
        item.requestStatusCount404 = spider_stats['downloader/response_status_count/404'] if 'downloader/response_status_count/404' in spider_stats else 0
        item.dupeFiltered = spider_stats['request_depth_max'] if 'request_depth_max' in spider_stats else 0
        item.imgCount = spider_stats['images_count'] if 'images_count' in spider_stats else 0
        item.nbScrapedItems = spider_stats['item_scraped_count'] if 'item_scraped_count' in spider_stats else 0
        # try:
        #     item.Crawler = Crawler.objects.get(nameCrawler=spider.name)
        # except MultipleObjectsReturned:
        #     print "Warning. get() return more than one Crawler. Taking the first one."
        #     item.Crawler = Crawler.objects.get(nameCrawler=spider.name)[0]

        item.save()
