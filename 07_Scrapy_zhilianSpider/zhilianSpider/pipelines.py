# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import datetime


class ZhilianspiderPipeline(object):
    def __init__(self):
        dt = datetime.datetime.now().strftime('%Y_%m_%d')
        # self.file = open('jobs_' + dt + '.txt', 'w', encoding='utf-8')
        self.conn = pymysql.connect(
            host='127.0.0.1',
            user='root',
            passwd='666666',
        )
        self.conn.query('create database if not exists zhilian')
        self.conn.commit()
        self.conn.close()
        self.conn1 = pymysql.connect(
            host='127.0.0.1',
            user='root',
            passwd='666666',
            db='zhilian',
            charset='utf8'
        )
        self.table_name = dt
        self.conn1.query('drop table if exists ' + self.table_name)
        self.conn1.commit()
        self.conn1.query(
            'create table ' + self.table_name + ' (title char(45),company char(40),salary char(20),address char(40),time char(15))'
        )
        self.conn1.commit()
        self.sql = 'insert into ' + self.table_name + '(title,company,salary,address,time) values("{title}","{company}","{salary}","{address}","{time}")'

    def process_item(self, item, spider):
        # self.file.write(item['title'] + '\t' +
        #                 item['company'] + '\t' +
        #                 item['salary'] + '\t' +
        #                 item['address'] + '\t' +
        #                 item['release'] + '\n')
        self.conn1.query(
            self.sql.format(
                title=item['title'],
                company=item['company'],
                salary=item['salary'],
                address=item['address'],
                time=item['release']
            )
        )
        self.conn1.commit()
        return item

    def spider_closed(self, spider):
        # self.file.close()
        self.conn1.close()

