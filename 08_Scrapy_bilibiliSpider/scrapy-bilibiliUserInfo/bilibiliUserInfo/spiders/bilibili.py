# -*- coding: utf-8 -*-
import scrapy
from bilibiliUserInfo.items import BilibiliuserinfoItem
import json

class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['bilibili.com']   
    userinfo_url = 'http://space.bilibili.com/ajax/member/GetInfo'
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin':'https://space.bilibili.com',
    'Referer':'',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':'',
    }

    def start_requests(self):
        url = 'https://www.bilibili.com'
        yield scrapy.Request(url,headers=self.headers,meta={'cookiejar':1},callback=self.parse)

    def parse(self,response):
    	for userid in range(10000000,11000000):
    		body = {
    		'mid':str(userid),
    		'csrf':'null'
    		}
    		self.headers['Referer'] = 'https://space.bilibili.com/' + str(userid)
    		yield scrapy.FormRequest(self.userinfo_url,headers=self.headers,formdata=body,meta={'cookiejar':response.meta['cookiejar']},callback = self.bilibiliUserInfoparse)

    	print("Done!")


    def bilibiliUserInfoparse(self, response):
        item = BilibiliuserinfoItem()
        r = json.loads(response.text)
        if response.status == 200 and r['status'] != False:
            data = r['data']
            print(data['mid'])
            for key in item.fields:
            	if key in data.keys():
            		item[key] = data.get(key)
            yield item
