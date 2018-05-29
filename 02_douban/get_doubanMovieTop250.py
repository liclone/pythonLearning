# -*- coding: utf-8 -*-
import re
import urllib.request
import time


def pretend():
    headers = {
        'Accept':
        'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':
        'gb2312,utf-8',
        'Accept-Language':
        'zh-CN,zh;q=0.8',
        'Connection':
        'keep-alive',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235',
    }
    opener = urllib.request.build_opener()
    headall = []
    for key, value in headers.items():
        item = (key, value)
        headall.append(item)
    opener.addheaders = headall
    urllib.request.install_opener(opener)


def getPage(page):
    url = 'https://movie.douban.com/top250?start='
    movielistpat = '<ol class="grid_view">(.+?)<div class="paginator">'
    data = urllib.request.urlopen(url + str(page)).read().decode(
        'utf-8', errors='ignore')
    return re.compile(movielistpat, re.S).findall(data)[0]


def getMovieInfo():
    movieinfopat = re.compile(
        '<em class="">(.*?)</em>.*?' + '<span class="title">(.*?)</span>.*?'
        # +'<span class="title">&nbsp;/&nbsp;(.*?)</span>.*?'
        + '<span class="other">&nbsp;/&nbsp;(.*?)</span>.*?' +
        '导演: (.*?)&nbsp.*?' +
        '(\d.*?)&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;(.*?)\n.*?</p>.*?' +
        'property="v:average">(.*?)</span>.*?' +
        'content="10.0"></span>.*?<span>(.*?)人评价</span>.*?' +
        '<span class="inq">(.*?)</span>',
        re.S)
    f = open('doubanMovieTop250.txt', 'w', encoding='utf-8')
    for page in range(11):
        data = getPage(page * 25)
        movies = re.findall(movieinfopat, data)
        for movie in movies:
            f.write('电影排名：' + movie[0] + '\n')
            f.write('电影名称：' + movie[1] + '\n')
            f.write('电影别名：' + movie[2] + '\n')
            f.write('导演姓名：' + movie[3] + '\n')
            f.write('上映时间：' + movie[4] + '\n')
            f.write('制作国家/地区：' + movie[5] + '\n')
            f.write('电影类别：' + movie[6] + '\n')
            f.write('电影评分：' + movie[7] + '\n')
            f.write('评价人数：' + movie[8] + '\n')
            f.write('简短影评：' + movie[9] + '\n\n')
        print('完成%d%%' % (page * 10))
    f.close()
    print('完毕')


def main():
    time.clock()
    pretend()
    getMovieInfo()
    print('用时%.2f秒' % (time.clock()))


if __name__ == '__main__':
    main()
