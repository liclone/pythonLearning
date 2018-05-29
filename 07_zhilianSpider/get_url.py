# -*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup


def get_url():
    url = 'http://jobs.zhaopin.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    #获取城市列表
    cities = soup.find_all('div', attrs={"class": "rightTab"})[0].find_all('a')
    with open('url_city.txt', 'w') as f:
        for city in cities:
            f.write('http:' + city['href'] + '\n')
    #获取行业列表
    industries_1 = soup.find_all('p', attrs={'class': 'hot_zq'})[0].find_all('a')
    industries_2 = soup.find_all('div', attrs={'class': 'hot_jobs'})[0].find_all('a')
    industries = industries_1 + industries_2
    with open('url_industry.txt', 'w') as f:
        for industry in industries:
            f.write(industry['href'] + '\n')
    #获取职位列表
    jobs_all = soup.find_all('div', attrs={'class': 'listcon'})
    jobs = []
    for i in jobs_all:
        jobs += i.find_all('a')
    with open('url_job.txt', 'w') as f:
        for job in jobs:
            f.write('http://jobs.zhaopin.com/' + job['href'] + '\n')

    print('URLs READY ! ')


if __name__ == '__main__':
    get_url()
