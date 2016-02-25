# coding=utf-8
'''
Created on 2016年2月22日

@author: kaka
'''
import json  
import codecs 
from .checkpipe import  check_spider_pipeline 
class JsonWithEncodingTencentPipeline(object):  
    pipeline = set([])
    def __init__(self):  
        self.file = codecs.open('tencent.json', 'w', encoding='utf-8')  
        
    @check_spider_pipeline 
    def process_item(self, item, spider):  
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"  
        self.file.write(line)  
        return item  
  
    def spider_closed(self, spider):  
        self.file.close() 
        
        
        
        