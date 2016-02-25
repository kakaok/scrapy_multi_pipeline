# -*- coding: utf-8 -*-
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
    
#     def parse_info(self,response):
#         it=BotItem()
#         it['titles']=response.selector.xpath('/html/head/title').extract()
#         it['texts']=response.selector.xpath('//div[@id="cnblogs_post_body"]//p/text()').extract()
#         self.json=open('it.json','w+')
#         ft=json.dumps(dict(it),ensure_ascii=True)+"\n" 
#         self.json.write(ft)
#         return it
#         print(response.selector.xpath('//div[@id="cnblogs_post_body"]//p/text()').extract())
#         print(response.selector.xpath('//a[@id="cb_post_title_url"]/text()').extract())
#         print(response.selector.xpath('/html/head/title').extract())
#         print(response.body)
#         print(response.selector.xpath('//div[@id="topics"]/div[@class="post"]/div[@class="post"]/h1/a/text()').extract_first())
#         print(dir(response.selector))
#         title=response.xpath('//div[@class="post"]/div[@class="post"]/h1/a/text()').extract_first()
#         url=response.xpath('//div[@class="post"]/div[@class="post"]/h1/a/@href').extract_first()
#         print title,url

    def parse_item(self, response):
        sel=response.selector
        posts=sel.xpath('//div[@id="mainContent"]/div/div[@class="day"]')
        items = []
        for p in posts:
            item = BotcnblogsItem()
            publishDate = p.xpath('div[@class="dayTitle"]/a/text()').extract_first()
            item["publishDate"] = (publishDate is not None and [publishDate.encode("utf-8")] or [""])[0]
            title = p.xpath('div[@class="postTitle"]/a/text()').extract_first()
            item["title"] = (title is not None and [title.encode("utf-8")] or [""])[0]
            readcount  = p.xpath('div[@class="postDesc"]/text()').re_first(u"阅读\(\d+\)")
            regReadCount = re.search(r"\d+", readcount)
            if regReadCount is not None:
                readcount = regReadCount.group()
            item["readCount"] = (readcount is not None and [readcount.encode("utf-8")] or [0])[0]
            commentcount  = p.xpath('div[@class="postDesc"]/text()').re_first(u"评论\(\d+\)")
            regCommentCount = re.search(r"\d+", commentcount)
            if regCommentCount is not None:
                commentcount = regCommentCount.group()
            item["commentCount"] = (commentcount is not None and [commentcount.encode("utf-8")] or [0])[0]
            items.append(item)
            
        return items
 
