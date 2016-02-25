# scrapy_multi_pipeline
处理scrapy中包括多个pipeline时如何让spider执行制定的pipeline管道
１:创建一个装饰器
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

2:在每个spider所在的类中添加一个pipeline数组，里面包含要执行的pipeline的名字
 -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider,Rule
# from scrapy.selector import Selector
from ..items import BotcnblogsItem,BotItem
from scrapy.linkextractors import LinkExtractor
import re
from ..BotcnblogsPipeline import BotcnblogsPipeline

class CnblogsSpider(CrawlSpider):
    pipeline = set([BotcnblogsPipeline,])
    #爬虫名称
    name = "cnblogs"
    #设置允许的域名
    allowed_domains = ["cnblogs.com"]
    #设置开始爬去的页面
    start_urls = (
        'http://www.cnblogs.com/fengzheng/',
    )
    
    rules=(
           Rule(LinkExtractor(allow=('fengzheng/default.html\?page\=([\d]+)')),callback='parse_item',follow=True),
#            Rule(LinkExtractor(allow=('fengzheng/p/([\d]+).html')),callback='parse_info',follow=True),
           )
           
3:在要执行的pipeline中的process_item方法加上装饰器，这样就可以过滤pipeline了

import json
from .checkpipe import  check_spider_pipeline 
class BotcnblogsPipeline(object):
    
    def __init__(self):
        self.file=open('jd.json','w+')
        
    @check_spider_pipeline
    def process_item(self,item,spider):
        #此处如果有中文的话，要加上ensure_ascii=False参数，否则可能出现乱码
        record=json.dumps(dict(item),ensure_ascii=False)+"\n" 
        self.file.write(record)
        return item
    
    def open_spider(self,spider):
        print("打开爬虫了")
        
    def close_spider(self,spider):
        print("关闭爬虫")
        self.file.close()
           
           

