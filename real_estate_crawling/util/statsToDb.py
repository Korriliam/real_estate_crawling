from __future__ import unicode_literals
# -*- coding: utf8 -*-

__author__ = 'Guillaume Le Bihan'

from location.models import Statistic
from real_estate_crawling.util import utc2local
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from django.core.exceptions import MultipleObjectsReturned
import scrapy

class statsToDb(scrapy.statscollectors.MemoryStatsCollector):
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


    def stats_spider_closed(self, spider):
        """
        this function is called whenever the spider is done with its work
        """
        item = Statistic()
        # on recupere certaines statistiques qui sont contenues dans un tableau nommé self.spider_stats.
        item.startTime  = unicode(self.utc2local(self.spider_stats['start_time']).replace(microsecond=0))
        item.finishTime = unicode(self.utc2local(self.spider_stats['finish_time']).replace(microsecond=0))
        item.finishReason = self.spider_stats['finish_reason'].encode('utf-8') if 'finish_reason' in self.spider_stats else 0
        item.requestBytes = self.spider_stats['downloader/request_bytes'] if 'downloader/request_bytes' in self.spider_stats else 0
        item.responseBytes = self.spider_stats['downloader/response_bytes'] if 'downloader/response_bytes' in self.spider_stats else 0
        item.requestCount = self.spider_stats['downloader/request_count'] if 'downloader/request_count' in self.spider_stats else 0
        item.responseCount = self.spider_stats['downloader/response_count'] if 'downloader/response_count' in self.spider_stats else 0
        item.responseReceivedCount = self.spider_stats['response_received_count'] if 'response_received_count' in self.spider_stats else 0
        item.requestDepthMax = self.spider_stats['request_depth_max'] if 'request_depth_max' in self.spider_stats else 0
        item.requestStatusCount200 = self.spider_stats['downloader/response_status_count/200'] if 'downloader/response_status_count/200' in self.spider_stats else 0
        item.requestStatusCount301 = self.spider_stats['downloader/response_status_count/301'] if 'downloader/response_status_count/301' in self.spider_stats else 0
        item.requestStatusCount302 = self.spider_stats['downloader/response_status_count/302'] if 'downloader/response_status_count/302' in self.spider_stats else 0
        item.requestStatusCount500 = self.spider_stats['downloader/response_status_count/500'] if 'downloader/response_status_count/500' in self.spider_stats else 0
        item.requestStatusCount404 = self.spider_stats['downloader/response_status_count/404'] if 'downloader/response_status_count/404' in self.spider_stats else 0
        item.dupeFiltered = self.spider_stats['request_depth_max'] if 'request_depth_max' in self.spider_stats else 0
        item.imgCount = self.spider_stats['images_count'] if 'images_count' in self.spider_stats else 0
        item.nbScrapedItems = self.spider_stats['item_scraped_count'] if 'item_scraped_count' in self.spider_stats else 0

        item.save()
