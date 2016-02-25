# coding=utf-8
'''
Created on 2016年2月24日

@author: kaka
'''
from scrapy.exceptions import DropItem
import functools
'''
当有多个pipeline时,判断spider如何执行指定的管道
'''
def check_spider_pipeline(process_item_method):
    @functools.wraps(process_item_method) 
    def wrapper(self, item, spider):
        # message template for debugging
        msg = '%%s %s pipeline step' % (self.__class__.__name__,)
        if self.__class__ in spider.pipeline:#判断要执行的spider中是否包含所需的pipeline　如果有则执行否则抛出DropItem信息
            spider.logger.debug(msg % 'executing')
            return process_item_method(self,item,spider)
        # otherwise, just return the untouched item (skip this step in
        # the pipeline)
        else:
            spider.logger.debug(msg % 'skipping')
            raise DropItem("Missing pipeline property")
    return wrapper

