# -*- coding: utf-8 -*-
import scrapy
from bilibiliVideoInfo.items import BilibilivideoinfoItem
import json
# import requests
# from bs4 import BeautifulSoup


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['bilibili.com']
    url_videoInfo = 'https://api.bilibili.com/x/web-interface/archive/stat?aid={aid}'
    # url_videoName = 'https://www.bilibili.com/video/av{aid}'
    headers = {
        'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':
        'gzip, deflate, sdch, br',
        'Accept-Language':
        'zh-CN,zh;q=0.8',
        'Connection':
        'keep-alive',
        'Content-Type':
        'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin':
        'https://www.bilibili.com',
        'X-Requested-With':
        'XMLHttpRequest',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.3',
    }

    def start_requests(self):
        for aid in range(100000,200000):
            print(aid)
            yield scrapy.Request(
                self.url_videoInfo.format(aid=aid),
                headers=self.headers,
                callback=self.parse)

    def parse(self, response):
        item = BilibilivideoinfoItem()
        r = json.loads(response.text)
        if r['code'] == 0 and response.status == 200:
            data = r['data']
            item['aid'] = data['aid']
            item['view'] = data['view']
            item['danmaku'] = data['danmaku']
            item['favorite'] = data['favorite']
            item['coin'] = data['coin']
            item['share'] = data['share']
            item['reply'] = data['reply']
            # item['name'] = BeautifulSoup(
            #     requests.get(self.url_videoName.format(aid=data['aid'])).text,
            #     'html.parser').head.title.text.rstrip('_哔哩哔哩 (゜-゜)つロ 干杯~-bilibili')
            # print(item)
            yield item
