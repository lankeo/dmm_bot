# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from dnn.user_config import db


class DnnPipeline(object):
    def open_spider(self, spider):
        client = MongoClient(host=db.get('host'), port=db.get('port'))
        self.collections = client[db.get('db_name')][spider.name]
    
    def close_spider(self, spider):
        count = self.collections.count()
        print("共%s条数据" % count)

    def process_item(self, item, spider):
        print(item)
        self.collections.insert(item)
        return item
    
