# coding=utf-8
'''
Created on 2016年2月19日

@author: kaka
'''
from scrapy.spiders import Spider
# import re 
from ..items import DoubanImgsItem
# from scrapy.http import Request
 
class download_douban(Spider):
    name="doubanimg"
    allowed_domains=['douban.com']
    url='152686895'
    start_urls=[
                'http://www.douban.com/photos/album/%s/' %(url,)
                ]
    
#     def __init__(self,url='152686895',*args,**kwargs):
#         self.allowed_domains=['douban.com']
#         self.start_urls=[
#                         'http://www.douban.com/photos/album/%s/' %(url)
#                         ]
#         self.url=url
#         super(download_douban,self).__init__(args,kwargs)
        
        
    def parse(self, response):
        list_imgs=response.xpath('//div[@class="photolst clearfix"]//img/@src').extract()
        if list_imgs:
            item=DoubanImgsItem()
            item['image_urls']=list_imgs
            yield item
        
