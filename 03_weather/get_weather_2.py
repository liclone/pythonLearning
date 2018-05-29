# -*-coding:utf-8-*-
import requests
import re
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235',
    'Accept-encoding': 'utf-8'
}


def get_city_code(city):
    city_pattern = re.compile(u"[\u4e00-\u9fa5]+")
    with open('CityCode.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if city == re.findall(city_pattern, line)[0]:
                return line.split()[-1]
            if line == lines[-1]:
                return 0


def get_weather(city_code):
    url = 'http://www.weather.com.cn/weather/' + city_code + '.shtml'
    response = requests.get(url, headers=HEADERS).content.decode('utf-8')
    soup = BeautifulSoup(response, 'html.parser')
    for w in soup.find_all('div', id='7d')[0].ul.find_all('li'):
        print(w.h1.string + w.p.string, end='\t')
        print(str(w.i.string) + '-' + str(w.span.string), end=' ')
        win = w.em.find_all('span')
        if len(win) == 1:
            print(win[0]['title'], end=' ')
        else:
            win1 = win[0]['title']
            win2 = win[1]['title']
            if win1 == win2:
                print(win1, end=' ')
            else:
                print(win1, win2, end=' ')
        print(w.find_all('i')[-1].string)


def main():
    city = input('请输入查询城市：')
    city_code = get_city_code(city)

    if city_code:
        get_weather(city_code)
    else:
        print('没有该城市')


if __name__ == '__main__':
    main()


