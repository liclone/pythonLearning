# -*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup


def get_download_url(url):
    download_url = []
    download_name = []
    server = 'http://www.biqukan.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }
    req = requests.get(url, headers=headers).text
    div = BeautifulSoup(req, 'lxml').find_all('div', class_='listmain')[0]
    a = div.find_all('a')
    for i in a:
        download_name.append(i.text)
        download_url.append(server + i.get('href'))
    return download_url, download_name


def get_contents(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }
    req = requests.get(url, headers=headers).text
    txt = BeautifulSoup(req, 'lxml').find_all('div', class_='showtxt')[0].text.replace('\xa0'*8, '\n\n')
    text = txt.rstrip(url + '　　请记住本书首发域名：www.biqukan.com。笔趣阁手机版阅读网址：m.biqukan.com')
    return text


def main():
    url = 'http://www.biqukan.com/11_11745/'
    name_novel = '复兴之路'
    urls, names = get_download_url(url)
    le = len(urls)
    with open(name_novel + '.txt', 'w', encoding='utf-8') as f:
        for i in range(14, le):
            print(names[i])
            print('已下载：%.1f%%' % ((i - 14) / (le - 14) * 100))
            f.write(names[i])
            f.write(get_contents(urls[i]) + '\n\n\n')
    print('Done!')


if __name__ == '__main__':
    main()
