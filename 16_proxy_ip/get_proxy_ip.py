# -*-coding:utf-8-*-
import time
import requests
from bs4 import BeautifulSoup
from config import *
import queue
from threading import Thread
import random
import os
from multiprocessing import Pool


class Verify(Thread):
    def __init__(self, ipque):
        Thread.__init__(self)
        self.ipque = ipque

    def run(self):
        n = 0
        while self.ipque.empty():
            time.sleep(2)
        while not self.ipque.empty():
            ip = self.ipque.get()
            proxy = {'http': 'http://'+ip,
                     'https': 'https://'+ip}
            try:
                response = requests.get(random.choice(VERIFY_URL), headers=HEADERS, proxies=proxy, timeout=3)
                print(ip + ' succeed !')
                with open('ip_available.txt', 'a+') as f:
                    f.write(ip + '\n')
            except:
                pass
            finally:
                n += 1
                if n == 15:
                    print('Running...')
                    n = 0


def get_ip(func):
    def wrapper():
        ipque = queue.Queue()
        print('get ' + func.__name__ + '\'s ip...')
        func(ipque)
        print('verify ' + func.__name__ + '\'s ip ...')
        thread = []
        for i in range(VERIFY_THREAD_NUM):
            thread.append(Verify(ipque))
        for th in thread:
            th.start()

    return wrapper


@get_ip
def xici(ipque):
    for i in range(1, XICI['page']+1):
        response = requests.get(url=XICI['url'] + str(i), headers=HEADERS).text
        soup = BeautifulSoup(response, 'html.parser')
        ips_info = soup.find('table', id='ip_list').find_all('tr')[1:]
        for ip_info in ips_info:
            ip = ip_info.find_all('td')
            ipque.put(ip[1].string + ':' + ip[2].string)


@get_ip
def ip66(ipque):
    for i in range(1, IP66['area']+1):
        for j in range(1, IP66['page']+1):
            response = requests.get(IP66['url'].format(area=str(i), page=str(j)),
                                    headers=HEADERS).text
            soup = BeautifulSoup(response, 'html.parser')
            ips_info = soup.find_all('tr')[2:]
            for ip_info in ips_info:
                ip = ip_info.find_all('td')
                ipque.put(ip[0].string + ':' + ip[1].string)


@get_ip
def kuaidaili(ipque):
    for i in range(1, KUAIDAILI['page']+1):
        response = requests.get(KUAIDAILI['url']+str(i), headers=HEADERS).text
        soup = BeautifulSoup(response, 'html.parser')
        ips_info = soup.find('div', id='list').table.tbody.find_all('tr')
        for ip_info in ips_info:
            ip = ip_info.find_all('td')
            ipque.put(ip[0].string + ':' + ip[1].string)

        time.sleep(1)  # 避免抓取过快被禁


@get_ip
def ip3366(ipque):
    for i in range(1, IP3366['page']+1):
        response = requests.get(IP3366['url']+str(i), headers=HEADERS).text
        soup = BeautifulSoup(response, 'html.parser')
        ips_info = soup.find('div', id='list').tbody.find_all('tr')
        for ip_info in ips_info:
            ip = ip_info.find_all('td')
            ipque.put(ip[0].string + ':' + ip[1].string)

        time.sleep(0.1)


def main():
    if os.path.exists('ip_available.txt'):
        os.remove('ip_available.txt')
    print('Start at ' + time.strftime('%Y-%m-%d %X', time.localtime()))
    time.clock()

    p = Pool(3)
    p.apply_async(xici())
    p.apply_async(ip3366())
    p.apply_async(ip66())
    # p.apply_async(kuaidaili())  # 快代理出现了问题，浏览器也无法打开
    p.close()
    p.join()
    '''
    计划全部线程结束后运行下方注释的程序
    实际为线程仍在验证IP时，下面的程序也运行了
    测试当进程中没有开线程时，.join()能阻碍程序进行，直到进程运行完再运行下方的程序
    
    '''
    # print('\nAll Done !!!')
    # print('End at ' + time.strftime('%Y-%m-%d %X', time.localtime()))
    # print('Take ' + str(time.clock()) + ' seconds')
    # if os.path.exists('ip_available.txt'):
    #     print('Available IP :')
    #     with open('ip_available.txt', 'r') as f:
    #         print(f.read())
    # else:
    #     print('No Available IP')


if __name__ == '__main__':
    main()

