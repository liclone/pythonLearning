# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
import datetime


class BilibilivideoinfoPipeline(object):
    def __init__(self):
        dt = datetime.datetime.now()
        self.conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            passwd='666666',
        )
        self.conn.query('create database if not exists bilibiliVideoInfo ')
        self.conn.commit()
        self.conn.close()
        self.conn1 = pymysql.connect(
            host='127.0.0.1',
            user='root',
            passwd='666666',
            db='bilibiliVideoInfo',
            charset='utf8')
        self.table_name = dt.strftime('%Y_%m_%d')
        self.conn1.query('drop table if exists ' + self.table_name)
        self.conn1.commit()
        sql_create_table = 'create table ' + self.table_name + '(aid int(32),view int(32),danmaku int(32),favorite int(32),share int(32),coin int(16),reply int(16))'
        self.conn1.query(sql_create_table)
        self.conn1.commit()
        self.sql = 'insert into ' + self.table_name + '(aid,view,danmaku,favorite,share,coin,reply) values("{aid}","{view}","{danmaku}","{favorite}","{share}","{coin}","{reply}")'

    def process_item(self, item, spider):
        self.conn1.query(
            self.sql.format(
                aid=item['aid'],
                view=item['view'],
                danmaku=item['danmaku'],
                favorite=item['favorite'],
                share=item['share'],
                coin=item['coin'],
                reply=item['reply']))
        self.conn1.commit()

    def close_spider(self, spider):
        self.conn1.close()
