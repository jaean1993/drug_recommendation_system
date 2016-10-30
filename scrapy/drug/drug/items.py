# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DrugItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    illness = scrapy.Field()
    link = scrapy.Field()
    drug_link = scrapy.Field()
    page_link = scrapy.Field()
    drug_name = scrapy.Field()
    pass

