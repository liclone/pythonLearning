# -*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup as bs
import threading
from city_industry import CITY, INDUSTRY
import time
import pymysql


class GetJobInfo(threading.Thread):
    def __init__(self, city_code, job_type, conn, sql_insert):
        threading.Thread.__init__(self)
        self.city_code = city_code
        self.job_type = job_type
        self.conn = conn
        self.sql_insert = sql_insert
        self.stopped = False
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
            'Host': 'www.liepin.com',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive'
        }
        self.url = 'https://www.liepin.com/zhaopin/?dqs={city_code}&industries={job_type}&curPage={page}'

    def stop(self):
        self.stopped = True

    def get_page(self, url):
        try:
            response = requests.get(url, headers=self.headers, timeout=5)
            soup = bs(response.text, 'lxml')
            jobs = soup.find_all('div', class_='sojob-item-main clearfix')
            if len(jobs) < 5:
                self.stop()
                self.conn.close()
            for job in jobs:
                try:
                    sql = self.sql_insert.format(
                        job=job.find('a', attrs={'data-promid': True}).text.strip(),
                        pay=job.find_all('span')[0].text,
                        place=job.find('a', attrs={'data-selector': 'data-url'}).text,
                        edu=job.find_all('span')[1].text,
                        experience=job.find_all('span')[2].text,
                        company=job.find('a', attrs={'title': True}).text.strip(),
                    )
                    self.conn.query(sql)
                    self.conn.commit()
                except:
                    pass
        except Exception as e:
            # print(e)
            pass

    def run(self):
        for i in range(100):
            self.get_page(self.url.format(city_code=self.city_code, job_type=self.job_type, page=i))
            print(i)
            time.sleep(1)


def create_database(database):
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='666666'
    )
    conn.query('create database if not exists ' + database)
    conn.commit()
    conn.close()


def create_table(database, table):
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='666666',
        db=database,
        charset='utf8'
    )
    conn.query('drop table if exists ' + table)
    conn.commit()
    conn.query('create table ' + table + '(job char(40),pay char(25),place char(40),edu char(20),experience char(20),company char(40))')
    conn.commit()
    conn.close()


def main():
    cities = ['北京', '上海', '广州', '深圳', '天津', '南京', '杭州']
    industries = ['IT服务', '电子', '工业自动化']

    database = 'job_info_liepin'
    create_database(database)
    t = time.strftime('%Y_%m_%d', time.localtime(time.time()))
    threads = []
    for i in range(len(industries)):
        table = industries[i] + '_' + t
        create_table(database, table)
        sql_insert = "insert into " + table + "(job,pay,place,edu,experience,company) values('{job}','{pay}','{place}','{edu}','{experience}','{company}')"

        for j in range(len(cities)):
            conn = pymysql.connect(
                host='127.0.0.1',
                user='root',
                passwd='666666',
                db=database,
                charset='utf8'
            )
            job = GetJobInfo(CITY[cities[j]], INDUSTRY[industries[i]], conn, sql_insert)
            threads.append(job)
            print('threading - ' + cities[j] + ' - ' + industries[i] + ' is ready ')

    for i in range(len(threads)):
        threads[i].start()
    for i in range(len(threads)):
        threads[i].join()

    print('Done!')


if __name__ == '__main__':
    main()

