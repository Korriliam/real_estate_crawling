from __future__ import unicode_literals
# -*- coding: utf8 -*-

__author__ = 'korriliam'

import random
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
from scrapy import log
from location.models import UserAgent

'''
    Mainly inspired from http://tangww.com/2013/06/UsingRandomAgent/
'''

class RotateUserAgent(UserAgentMiddleware):
    user_agent_list = []
    user_agent = ""
    def __init__(self, user_agent=''):
        ua = UserAgent.objects.all()
        for elmt in ua:
            self.user_agent_list.append(elmt.user_agent_string)

    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_list)
        if ua:
            request.headers.setdefault('User-Agent', ua)
            # Add desired logging message here.
            spider.log(
                u'User-Agent: {} {}'.format(request.headers.get('User-Agent'), request),
                level=log.DEBUG
            )
