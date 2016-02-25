# coding=utf-8
'''
Created on 2016年2月22日

@author: kaka
'''
import json
from .checkpipe import  check_spider_pipeline 
class BotcnblogsPipeline(object):
    
    def __init__(self):
        self.file=open('jd.json','w+')
#         self.json=open('it.json','w+')
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