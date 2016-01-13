# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import logging

from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log

class DomainNameScraperPipeline(object):
    def process_item(self, item, spider):
        return item

import collections
def _remove_empty(li):
    if not isinstance(li, collections.Iterable):
        return li
    nli=[]
    for i in li:
        try:
            i=i.strip()
            if len(i)<3:
                i=""
        except:pass
        if not i: continue
        nli.append(i)
    return nli


def first(val):
    if isinstance(val, unicode) or isinstance(val, str):
        return val
    if isinstance(val, collections.Iterable):
        try: return val[0]
        except:pass
    return val


class PrepDataPipeline(object):
    def process_item(self, item, spider):
        item["word"] = first(item.get("word",["",]))
        item["pos"] = first(item.get("pos",["",]))
        item["neg"] = first(item.get("neg",["",]))
        item["meaning"] = _remove_empty(item.get("meaning",[]))
        item["example"] = _remove_empty(item.get("example",[]))
        
        return item
        
        
        
class MongoDBPipeline(object):

    def __init__(self, mongo_uri, mongo_db, collection_name):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.collection_name = collection_name

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGODB_DB'),
            collection_name = crawler.settings.get('MONGODB_COLLECTION_SCRAPED_DATA')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if not item.get("word",None):
            raise DropItem("Missing word")
        self.db[self.collection_name].insert(dict(item))
        return item