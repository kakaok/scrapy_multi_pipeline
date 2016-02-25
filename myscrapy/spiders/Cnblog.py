# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule
# from scrapy.http import Request
# from ..checkpipe import  check_spider_pipeline 
from ..items import  CnBlogItem
class CnblogSpider(CrawlSpider):
    pipeline = set([])
    name = "Cnblog"
    #设置下载延时  
    #download_delay = 3o 
    #设置域名
    allowed_domains = ["cnblogs.com"]
    start_urls = [
                  'http://www.cnblogs.com'
                ]
    rules=(
#             Rule(LinkExtractor(allow=('/cate/', ),deny=('/comment/'))),
           Rule(LinkExtractor(allow=('')),callback='parse_item',follow=True),
           )
    
    
#     def parse(self,response):
#         yield Request(response.url, callback=self.parse_item)
    
#     def parse_start_url(self, response):
#         print(response)
#         return CrawlSpider.parse_start_url(self, response)
    
#     def parse_sts(self,response):
#         post_item_list=response.xpath('//div[@class="post_item"]')
#         for it in post_item_list:
#             pt=CnBlogItem()
#             pt['title']=it.xpath('div[@class="post_item_body"]/h3/a/text()').extract()[0]
#             pt['url']=it.xpath('div[@class="post_item_body"]/h3/a/@href').extract()[0]
#             pt['text']=it.xpath('div[@class="post_item_body"]/p[@class="post_item_summary"]/text()').extract()
#             pt['user']=it.xpath('div[@class="post_item_body"]/div[@class="post_item_foot"]/a/text()').extract()
#             pt['datetime']=it.xpath('div[@class="post_item_body"]/div[@class="post_item_foot"]/text()').extract()
#             pt['discuss']=it.xpath('div[@class="post_item_body"]/div[@class="post_item_foot"]/span[@class="article_comment"]/a/text()').extract()
#             pt['readcount']=it.xpath('div[@class="post_item_body"]/div[@class="post_item_foot"]/span[@class="article_view"]/a/text()').extract()
#             print pt
#             yield pt
   
    def parse_item(self,response):
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
            return pt
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
     

    def parse(self, response):
        pass
