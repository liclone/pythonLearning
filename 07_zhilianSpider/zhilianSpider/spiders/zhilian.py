# -*- coding: utf-8 -*-
import scrapy
from zhilianSpider.items import ZhilianspiderItem
from scrapy import Request


class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    allowed_domains = ['zhaopin.com']
    start_urls = []

    def __init__(self):
        urls = open('F:/Github/zhilianSpider/url_city.txt')
        for url in urls:
            self.start_urls.append(url[:-1])

    def parse(self, response):
        item = ZhilianspiderItem()
        title_list = response.xpath('//div/span[@class="post"]/a/text()').extract()
        company_list = response.xpath('//div/span[@class="company_name"]/a/text()').extract()
        salary_list = response.xpath('//div/span[@class="salary"]/text()').extract()
        address_list = response.xpath('//div/span[@class="address"]/text()').extract()
        release_list = response.xpath('//div/span[@class="release_time"]/text()').extract()

        if response.xpath('//span[@class="search_page_next"]'):
            next_url = response.xpath('//span[@class="search_page_next"]/a/@href').extract()[0]
            yield Request('http://jobs.zhaopin.com' + next_url)

        print(response.url)

        for i in range(len(title_list)):
            item['title'] = title_list[i]
            item['company'] = company_list[i]
            item['salary'] = salary_list[i]
            item['address'] = address_list[i]
            item['release'] = release_list[i]
            # print(item)
            yield item

