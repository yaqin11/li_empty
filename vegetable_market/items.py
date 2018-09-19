# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VegetableMarketItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #菜市场名称
    name = scrapy.Field()
    #菜市场所在市区
    area_name = scrapy.Field()
    #菜市场所在街道
    address = scrapy.Field()
    #菜市场地址详情
    profile = scrapy.Field()
    #菜市场电话
    phone = scrapy.Field()
    

