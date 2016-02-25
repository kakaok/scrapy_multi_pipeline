# coding=utf-8
'''
Created on 2016年2月19日

@author: kaka
'''
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
# class DoubanImgsPipeline(object):
#     def process_item(self,item,response):
#         return item
    
    
class DouBanImgDownLoadPipeLine(ImagesPipeline):
    def get_media_requests(self,item,info):
        for  imgurl in item['image_urls']:
            yield Request(imgurl)
            
    def item_completed(self,requests,item,info):
        image_paths=[x['path'] for ok,x in requests if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths']=image_paths
        return item
            