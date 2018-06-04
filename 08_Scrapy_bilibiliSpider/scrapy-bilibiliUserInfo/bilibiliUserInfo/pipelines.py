# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
import pymysql


class BilibiliuserinfoPipeline(object):
    def __init__(self):
        dt = datetime.datetime.now()
        self.conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            passwd='666666',
        )
        self.conn.query('create database if not exists bilibiliUserInfo ')
        self.conn.commit()
        self.conn.close()

        self.conn1 = pymysql.connect(
            host='127.0.0.1',
            user='root',
            passwd='666666',
            db='bilibiliUserInfo',
            charset='utf8')
        self.table_name = dt.strftime('%Y_%m_%d')
        self.conn1.query('drop table if exists ' + self.table_name)
        self.conn1.commit()
        sql_create_table = 'create table ' + self.table_name + '(mid int(32),name char(16),sex char(8),playNum int(32),birthday char(16),place char(16))'
        self.conn1.query(sql_create_table)
        self.conn1.commit()

        self.sql = 'insert into ' + self.table_name + '(mid,name,sex,playNum,birthday,place) values("{mid}","{name}","{sex}","{playNum}","{birthday}","{place}")'

    def process_item(self, item, spider):
        self.conn1.query(
            self.sql.format(
                mid=item['mid'],
                name=item['name'],
                sex=item['sex'],
                playNum=item['playNum'],
                birthday=item['birthday'],
                place=item['place']))
        self.conn1.commit()

    def close_spider(self, spider):
        self.conn1.close()
