# -*- coding: utf-8 -*-
import urllib.request
import re


def getWeather(url):
    data = urllib.request.urlopen(url).read().decode("utf-8", errors="ignore")
    #获取7天的信息
    pat1 = '<div id="7d" class="c7d">.+?<div class="btn">'
    result1 = re.compile(pat1, re.S).findall(data)
    result1 = result1[0]
    #获取每天的信息
    pat2 = '<h1>.+?<div class="slid">'
    result2 = re.compile(pat2, re.S).findall(result1)

    daypat = '<h1>(.+?)</h1>'
    weatherpat = 'class="wea">(.+?)</p>'
    tempatL = '<p class="tem">.+?<i>(.+?)℃</i>'
    tempatH = '<p class="tem">\n<span>(.+?)</span>'
    winpat = '<span title="(.+?)"'
    winvalpat = '</em>\n<i>(.+?)</i>'

    for days in result2:
        day = re.compile(daypat).findall(days)[0]
        weather = re.compile(weatherpat).findall(days)[0]
        temL = re.compile(tempatL, re.S).findall(days)
        if temL == []:
            temL = 'None'
        else:
            temL = temL[0]
        temH = re.compile(tempatH, re.S).findall(days)
        if temH == []:
            temH = 'None'
        else:
            temH = temH[0]
        win = re.compile(winpat).findall(days)
        if len(win) > 1:
            if win[0] == win[1]:
                win1 = win[0]
            else:
                win1 = win[0] + "和" + win[1]
        else:
            win1 = win[0]
        winval = re.compile(winvalpat).findall(days)[0]

        print(day, weather + "\t" + temL + " 至 " + temH + "℃\t" + win1 + "\t" +
              winval)
        print("")


def getCityCode(city):
    # 匹配中文
    citypat = re.compile(u"[\u4e00-\u9fa5]+")
    codepat = "(\d+)"

    f = open("./CityCode.txt", 'r', encoding='utf-8')
    lines = f.readlines()
    for line in lines:
        if city == re.findall(citypat, line)[0]:
            f.close()
            return (re.findall(codepat, line)[0])
        if line == lines[-1]:
            f.close()
            return 0


def main():
    city = input("请输入查询城市名字：")
    code = getCityCode(city)
    if code == 0:
        print("没有该城市")
        return 0
    url = 'http://www.weather.com.cn/weather/' + code + ".shtml"
    getWeather(url)


if __name__ == "__main__":
    main()
