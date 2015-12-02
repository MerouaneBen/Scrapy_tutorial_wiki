# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class TutorialWikiItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank =Field()
    article = Field()
    link = Field()
    views = Field()
    periode = Field()

