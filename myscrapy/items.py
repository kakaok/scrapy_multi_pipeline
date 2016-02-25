# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import  Item,Field


class TencentItem(Item):  
    name = Field()                # 职位名称  
    catalog = Field()             # 职位类别  
    workLocation = Field()        # 工作地点  
    recruitNumber = Field()       # 招聘人数  
    detailLink = Field()          # 职位详情页链接  
    publishTime = Field()         # 发布时间  

#爬去文件内容
class DoubanImgsItem(Item):
    image_urls=Field()
    images=Field()
    image_paths=Field()

class CnBlogItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #定义要抓取的对象
    title=Field() #标题
    text=Field()#内容简介
    url=Field()#url
    datetime=Field() #发布时间
    user=Field()#发布用户
    discuss=Field()#评论
    readcount=Field()#阅读量
    
"""
爬取多个页面
"""
class BotcnblogsItem(Item):
    title=Field()# 标题
    publishDate=Field()#发布日期
    readCount=Field() #阅读量
    commentCount=Field() #评论量
    
class BotItem(Item):
    titles=Field()
    texts=Field()
    
