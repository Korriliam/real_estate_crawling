#!/bin/bash

cd /home/korriliam/real_estate_crawling/real_estate_crawling/
export DJANGO_SETTINGS_MODULE="real_estate_crawling.location.settings"
export PYTHONPATH=$PYTHONPATH:/home/korrigan/real_estate_crawling/
echo "Changing dir"
source ../bin/activate
echo "Launching spider"
echo $1
scrapy crawl $1
echo "ENDED"
