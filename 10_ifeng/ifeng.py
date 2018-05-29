# -*-coding:utf-8-*-
'''
获取凤凰网即时新闻界面的新闻
得到标题和链接及文章
'''
import requests
from lxml import etree
import time

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',

}

t = time.strftime('%Y%m%d', time.localtime())


# 得到相关内容
def get_main_content(url):
    response = requests.get(url, headers=HEADERS).content.decode('utf-8')
    root = etree.HTML(response)
    main_content = root.xpath('//div[@id="main_content"]//p')
    if main_content:
        for p in main_content:
            text = p.xpath('text()')
            if text:
                print(text[0])
            else:
                print('')
    else:
        wrap = root.xpath('//div[@class="wrapIphone AtxtType01"]//p')
        if wrap:
            for p in wrap:
                text = p.xpath('text()')
                if text:
                    print(text[0])
                else:
                    print('')
        else:
            ps = root.xpath('//div[@id="yc_con_txt"]//p')
            if ps:
                for p in ps:
                    text = p.xpath('text()')
                    if text:
                        print(text[0])
                    else:
                        print('')
            else:
                print('图片新闻，请查看链接')


def get_instant_news(tim, page):
    url = 'http://news.ifeng.com/listpage/11502/'+tim+'/'+str(page)+'/rtlist.shtml'
    response = requests.get(url, headers=HEADERS).content.decode('utf-8')
    root = etree.HTML(response)
    uls = root.xpath('//div[@class="newsList"]//ul')
    for ul in uls:
        for li in ul:
            print('----------------------------------------------------------')
            print(li.xpath('a/text()')[0] + '\t\t' + li.xpath('h4/text()')[0])
            print(li.xpath('a/@href')[0])
            # get_main_content(li.xpath('a/@href')[0])
            print('')

            time.sleep(0.1)

    a = root.xpath('//div[@class="m_page"]//a')
    for i in a:
        if i.xpath('text()')[0] == '下一页 ':
            get_instant_news(t, page+1)


if __name__ == '__main__':
    get_instant_news(t, 1)
