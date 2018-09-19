# -*- coding: utf-8 -*-
import scrapy
from vegetable_market.items import VegetableMarketItem
import json
import urllib.parse

city = str(input('请输入您要爬取的城市：'))
select_content = str(input('请输入您要查询的内容:'))

class HenanSpider(scrapy.Spider):
    name='henan'
    allowed_domains = ['map.baidu.com']
    #默认的编号为郑州的编号
    cid = 268

    # 定义解析文本的地址
    filename = 'E:\BaiduMap_cityCode_1102.txt' 

    citys = dict()

    with open(filename, 'r',encoding='utf8') as file_to_read:
      while True:
        # 整行读取数据
        lines = file_to_read.readline() 
        if not lines:
          break
        # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
        city_id,city_name = [str(i) for i in lines.split(',')]
        city_name = city_name.strip()
        citys[city_name] = city_id
      # print(citys)
    #获取输入的城市的编号
    for key,value in citys.items():
        if key == city:
            cid = int(citys[key])
            break
    print(cid) 

    select_content = urllib.parse.quote(select_content)
    print(select_content)

    start_urls = ['http://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=after_baidu&pcevaname=pc4.1&qt=con&from=webmap&c={cid}&wd={select_content}&wd2=&pn=0&nn=0&db=0&sug=0&addr=0'.format(cid = cid,select_content=select_content)]
    #start_urls = ['http://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=after_baidu&pcevaname=pc4.1&qt=con&from=webmap&c=268&wd=%E9%83%91%E5%B7%9E%E8%8F%9C%E5%B8%82%E5%9C%BA&wd2=&pn=0&nn=0&db=0&sug=0&addr=0']
    url = 'http://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=after_baidu&pcevaname=pc4.1&qt=con&from=webmap&c={cid}&wd={select_content}&wd2=&pn={page}'
    #url = 'http://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=after_baidu&pcevaname=pc4.1&qt=con&from=webmap&c=268&wd=%E9%83%91%E5%B7%9E%E5%B8%82%E8%8F%9C%E5%B8%82%E5%9C%BA&wd2=&pn={}'
    page=1
    # http://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=after_baidu&pcevaname=pc4.1
    # &qt=con&from=webmap&c=268&wd=%E9%83%91%E5%B7%9E%E8%8F%9C%E5%B8%82%E5%9C%BA&wd2=&pn=0&nn=0&db=0&sug=0
    # &addr=0&&&auth=4%40vAIIAd4VvA7bzZFYTaXI2PT3LWxYNOuxHBBHBHBHRtBnlQADZZz1GgvPUDZYOYIZuVt1cv3uVtcvY1SGpuEtSZz4JyBExc2us7i%3DsGIdddddddddFWvPYuxt8zv7u%40ZPuBt0x2whjzgjyBKEEKEEEBWxwAYYKi3rZZWuxx&device_ratio=1&tn=B_NORMAL_MAP&ie=utf-8&l=9&b=(12421519.499123711,4031960.8680412374;12779237.08768041,4129901.1155670104)&t=1533535395354
    # http://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=after_baidu&pcevaname=pc4.1
    # &qt=con&from=webmap&c=268&wd=%E9%83%91%E5%B7%9E%E8%8F%9C%E5%B8%82%E5%9C%BA&wd2=&pn=2&nn=10&db=0&sug=0
    # &addr=0&&&auth=4%40vAIIAd4VvA7bzZFYTaXI2PT3LWxYNOuxHBBHBLVzztzljPyBYYx1GgvPUDZYOYIZuVt1cv3uVtPWv3GuxLtrJj5cSEITHYAmk5b7kzC888888888yWvPYuxt8zv7u%40ZPuEthyHxhjzgjyBKEEKEEEBWxwAYYKi3rZZWuxz&device_ratio=1&tn=B_NORMAL_MAP&ie=utf-8&l=10&b=(12502636.518430656,4050384.4028832116;12731687.5479927,4115611.9654744524)&t=1533536272336
    # http://map.baidu.com/?newmap=1&reqflag=pcmap&biz=1&from=webmap&da_par=after_baidu&pcevaname=pc4.1
    # &qt=con&from=webmap&c=268&wd=%E9%83%91%E5%B7%9E%E8%8F%9C%E5%B8%82%E5%9C%BA&wd2=&pn=3&nn=20&db=0&sug=0
    # &addr=0&&&auth=4%40vAIIAd4VvA7bzZFYTaXI2PT3LWxYNOuxHBBHBLBzxtBnlQADZZz1GgvPUDZYOYIZuVt1cv3uVtPWv3GuxRt0KzxZnex3MhhhhhhhhhJWvPYuxt8zv7u%40ZPuHtizIygz%402VJtyBYxnpElp1GPJJPJJJG%40DwAYYKi3rZZWuxB&device_ratio=1&tn=B_NORMAL_MAP&ie=utf-8&l=10&b=(12456820.80264192,4075895.9532751087;12759865.39731441,4126699.183275108)&t=1533536463208
    def parse(self, response):
        # 解析内容,因为返回的是json格式数据，直接解析json格式即可
        # 将json数据转化为python对象
        data = json.loads(response.body_as_unicode())

        if self.page != 2:
        # 通过分析，要data里面的 content
            infos = data['content']
            num = 0
            for info in infos:
                num += 1
                if num <= 10:
                    # 创建对象
                    item = VegetableMarketItem()
                    #菜市场名称
                    item['name'] = info['name']
                    #菜市场所在市区
                    item['area_name'] = info['area_name']
                    #菜市场所在街道
                    item['address'] = info['addr']
                    #菜市场详细地址
                    if info.get('address_norm'):
                        item['profile'] = info.get('address_norm')
                    else:
                        item['profile'] = info['area_name'] + info['addr']

                    #菜市场的电话
                    if info.get('tel'):
                        item['phone'] = info['tel']
                    else:
                        item['phone'] = '无'
                    yield item
                else:
                    continue
        # 接着发送请求，爬取下一页
        self.page += 1
        url = self.url.format(cid = self.cid,select_content = self.select_content,page = self.page)
        #url = self.url.format(self.page)
        # 向拼接成功的url发送请求
        yield scrapy.Request(url, callback=self.parse)


    