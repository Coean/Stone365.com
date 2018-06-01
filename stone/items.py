# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StoneItem(scrapy.Item):
    company = scrapy.Field()
    name = scrapy.Field()
    tel = scrapy.Field()
    ph = scrapy.Field()
    fax = scrapy.Field()
    email = scrapy.Field()
    https = scrapy.Field()
    address = scrapy.Field()
