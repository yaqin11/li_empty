# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql
from scrapy.utils.project import get_project_settings
from vegetable_market.spiders.henan import city

class VegetableMarketPipeline(object):
    def open_spider(self, spider):
        #print('#'*10)
        self.fp = open('zhengzhou.txt', 'w', encoding='utf8')

    def process_item(self, item, spider):
        print('*'*10)
        obj = dict(item)
        string = json.dumps(obj, ensure_ascii=False)
        self.fp.write(string + '\n')
        return item

    def close_spider(self, spider):
        self.fp.close()

class MySqlPipeline(object):
  """docstring for MySql"""
  def open_spider(self, spider):
    # 连接数据库
    # self.conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='123456', db='movie', charset='utf8')

    # 将配置文件读到内存中，是一个字典
    settings = get_project_settings()
    host = settings['DB_HOST']
    port = settings['DB_PORT']
    user = settings['DB_USER']
    #password = settings['DB_PASSWORD']
    dbname = settings['DB_NAME']
    dbcharset = settings['DB_CHARSET']

    #self.conn = pymysql.Connect(host=host, port=port, user=user, password=password, db=dbname, charset=dbcharset)
    self.conn = pymysql.Connect(host=host, port=port, user=user, db=dbname, charset=dbcharset)
  def process_item(self, item, spider):
    #创建数据库
    database = 'create table  if not exists {city}_table(id int auto_increment,primary key(id), name varchar(200), area_name varchar(1000),route varchar(1000),profile varchar(1000), phone varchar(100))engine=innodb default charset=utf8;'.format(city = city)
    # 写入数据库中
    sql = 'insert into {city}_table(name,area_name,route, profile,phone) values("%s", "%s", "%s", "%s","%s")'.format(city = city) % (item['name'], item['area_name'],item['address'],item['profile'], item['phone'])
    # 执行sql语句
    self.cursor = self.conn.cursor()
    try:
      self.cursor.execute(database)
      self.cursor.execute(sql)
      print('#' * 10)
      print('写入成功！')
      self.conn.commit()
    except Exception as e:
      print('*' * 10)
      print('写入失败！')
      print(e)
      self.conn.rollback()

    return item

  def close_spider(self, spider):
    self.cursor.close()
    self.conn.close()