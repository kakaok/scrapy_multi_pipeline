#coding=utf-8
'''
Created on 2016年2月17日

@author: kaka
'''
import scrapy
from ..items import CnBlogItem
# from ..checkpipe import  check_spider_pipeline 
class CnBlogSpider(scrapy.Spider):
    pipeline = set([])
    name="cnblog"
    allowed_domains=["cnblogs.com"]
    start_urls=["http://www.cnblogs.com/cate/2"]
#     @check_spider_pipeline
    def parse(self,response):
        post_item_list=response.xpath('//div[@class="post_item"]')
        for it in post_item_list:
            pt=CnBlogItem()
            pt['title']=it.xpath('div[@class="post_item_body"]/h3/a/text()').extract()[0]
            pt['url']=it.xpath('div[@class="post_item_body"]/h3/a/@href').extract()[0]
            pt['text']=it.xpath('div[@class="post_item_body"]/p[@class="post_item_summary"]/text()').extract()
            pt['user']=it.xpath('div[@class="post_item_body"]/div[@class="post_item_foot"]/a/text()').extract()
            pt['datetime']=it.xpath('div[@class="post_item_body"]/div[@class="post_item_foot"]/text()').extract()
            pt['discuss']=it.xpath('div[@class="post_item_body"]/div[@class="post_item_foot"]/span[@class="article_comment"]/a/text()').extract()
            pt['readcount']=it.xpath('div[@class="post_item_body"]/div[@class="post_item_foot"]/span[@class="article_view"]/a/text()').extract()
            print pt
            yield pt
        
        
        
        
        
        