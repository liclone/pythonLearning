# -*-coding:utf-8-*-
from city_industry import INDUSTRY, CITY
import time
import pymysql
import matplotlib.pyplot as plt

t = time.strftime('%Y_%m_%d', time.localtime(time.time()))
config = {
    'host'   : '127.0.0.1',
    'user'   : 'root',
    'passwd' : '666666',
    'db'     : 'job_info_liepin',
    'charset': 'utf8',
}


def draw_bar_edu(data):
    edu = ['硕士', '本科', '大专', '不限']
    num = []
    for i in range(len(edu)):
        n = []
        for j, k in data.items():
            n.append(k[edu[i]])
        num.append(n)

    plt.xlabel('industry')
    plt.ylabel('number')
    plt.title('education needed')
    total_width, n = 0.5, len(data)
    width = total_width / n

    x = []
    for i in range(len(edu)):
        xx = []
        for j in range(len(data)):
            xx.append(i*width + j)
        x.append(xx)
    print(x)

    plt.bar(x[0], num[0], width=width, label='shuoshi')
    plt.bar(x[1], num[1], width=width, label='benke')
    plt.bar(x[2], num[2], width=width, label='dazhuan')
    plt.bar(x[3], num[3], width=width, label='buxian')

    plt.legend()
    plt.show()


def get_num(l, option):
    conn = pymysql.connect(**config)
    cursor = conn.cursor()
    data = {}
    for industry in INDUSTRY:
        data[industry] = ''
        table = industry + '_' + t
        data1 = {}
        for i in l:
            cursor.execute('select count(*) from ' + table + ' where ' + option + ' regexp "' + i + '"')
            data1[i] = cursor.fetchone()[0]
        data[industry] = data1
    conn.close()
    return data


def main():
    edu = ['硕士', '本科', '大专', '不限']
    city = []
    for i in CITY:
        city.append(i)
    company = ['某|知名']
    experience = ['不限', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    print(get_num(city, 'place'))
    print(get_num(company, 'company'))
    print(get_num(experience, 'experience'))
    draw_bar_edu(get_num(edu, 'edu'))


if __name__ == '__main__':
    main()
