real_estate_crawling
=============
Tool created for seeking property ads, in order to help me getting a decent flat in Paris (which is - soooo - difficult nowadays !)
Hoping these snippets could help some persons, in Paris or elsewhere ...

Instructions
-------------
1 - Clone this project ( Could you have guessed ? :P )
2 - Get MySql and create a schema whose name should be entered in spiders/settings.py and affected to DATABASE_SCHEMA
3 - execute the script manage.py as follow : *python manage.py syncdb*. This will create, inside the schema you've just created two tables:
- Statistics (as its named suggests, contains stats dealing with the crawls);
- Annonces (french for ads, will contains scraped adds)
4 - Execute one of those commands, based on the property ads website you want to scrape:
For http://www.pap.fr/ : *scrapy crawl pap1*
For http://www.leboncoin.fr/ : *scrap crawl lbc1*
For http://www.seloger.fr/ : *scrapy crawl seloger1*
Those will gather ads and fill up the database. Once its done, you'll be free to consult this data and to make your choice...
