# -*-coding:utf-8-*-

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gb2312,utf-8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235',
}

VERIFY_URL = [
    'http://www.baidu.com',
    'http://www.sina.com.cn/',
    'http://www.sohu.com/',
    'http://www.163.com/',
    'http://www.qq.com/',
    'https://www.hao123.com/'
]

VERIFY_THREAD_NUM = 8

XICI = {
    'url': 'http://www.xicidaili.com/nn/',
    'page': 2,  # 爬取页数，每页有100个IP

}

# 66ip网提供不同地点的IP,共33个地方
IP66 = {
    'url': 'http://www.66ip.cn/areaindex_{area}/{page}.html',
    'page': 1,
    'area': 34,
}

KUAIDAILI = {
    'url': 'https://www.kuaidaili.com/free/inha/',
    'page': 6
}

IP3366 = {
    'url': 'http://www.ip3366.net/?stype=1&page=',
    'page': 10
}