# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BilibilivideoinfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    aid = scrapy.Field()
    danmaku = scrapy.Field()
    favorite = scrapy.Field()
    share = scrapy.Field()
    coin = scrapy.Field()
    reply = scrapy.Field()
    view = scrapy.Field()

    
