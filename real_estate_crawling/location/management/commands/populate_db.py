from __future__ import unicode_literals
# -*- coding: utf8 -*-

from location.models import OfferType, UserAgent, Source

class Command(BaseCommand):

    args = '<ttt ttt ...>'
    help = 'Commands purpose is to replete the database'

    def _create_offer_types(self):
        type1 = OfferType()
        type1.name = 'location'
        type1.save()

        type2 = OfferType()
        type2.name = 'colocation'
        type2.save()

    def _create_user_agents(self):
        pass

    def _create_source(self):
        s1 = Source()
        s1.url = ""
        s1.name = "seloger"
        s1.save()

        s2 = Source()
        s2.url = ""
        s2.name = "pap"
        s2.save()

        s3 = Source()
        s3.url = ""
        s3.name = "leboncoin"
        s3.save()

# url = eli.thegreenplace.net/2014/02/15/programmatically-populating-a-django-database/
