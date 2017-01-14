from __future__ import unicode_literals
# -*- coding: utf8 -*-
__author__ = 'Guillaume LE Bihan'

from datetime import datetime
import time


def utc2local(self, utc):
    '''
    Convert universal time to local time (gmt + 2 (Paris))
    '''
    epoch = time.mktime(utc.timetuple())
    offset = datetime.fromtimestamp(epoch) - datetime.utcfromtimestamp(epoch)
    return utc + offset
