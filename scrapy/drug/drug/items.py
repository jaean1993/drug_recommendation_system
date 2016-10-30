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
    rx_otc = scrapy.Field()
    pregnancy = scrapy.Field()
    csa = scrapy.Field()
    alcohol = scrapy.Field()
    review_num = scrapy.Field()
    rating = scrapy.Field()
    popularity = scrapy.Field()

    pass

