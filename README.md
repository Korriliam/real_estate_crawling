real_estate_crawling
====================

Purpose
-------
Tool created for seeking property ads, in order to help me getting a decent flat in Paris (which is - soooo - difficult nowadays !)

Basically, we retrieve location and sale ads on five mainstream french real estate websites :
* leboncoin;
* seloger;
* logicimmo;
* explorimmo;
* pap;

Then, the scraped data is saved inside a database. From then on, Django's magic will enable us
to accurately see the gathered data in a django admin interface, and to filter out the adds.

For the moments, we just crawl offers throughout Paris, which give us a pretty critical amount of data,
suitable to tackle some data analysis task, we is yet to come.

Hoping these snippets could help some persons, in Paris or elsewhere ...

Installation
-------------
0. execute the script manage.py as follow : *python manage.py makemigrations*. This will create, inside the schema you've just created two tables:
- Statistics (as its named suggests, contains stats dealing with the crawls);
- Annonces (french for ads, will contains scraped adds)
0. Execute one of those commands, based on the property ads website you want to scrape:
For http://www.pap.fr/ : *scrapy crawl pap1*
For http://www.leboncoin.fr/ : *scrap crawl lbc1*
For http://www.seloger.fr/ : *scrapy crawl seloger1*
Those will gather ads and fill up the database. Once its done, you'll be free to consult this data and to make your choice...

Don't forget to launch tor and polipo !

Usage
-----

