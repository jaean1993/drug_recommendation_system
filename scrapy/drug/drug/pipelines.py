# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DrugPipeline(object):
    def __init__(self):
        self.file = open('drug.txt', mode='wb')
    def process_item(self, items, spider):

        return items
