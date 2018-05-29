import smtplib
from email.mime.text import MIMEText
import urllib.request
import json


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


def get_weather_info(city):
    pretend()
    try:
        weather_api = 'https://www.sojson.com/open/api/weather/json.shtml?city=' + urllib.request.quote(
            city)
        weather = json.loads(urllib.request.urlopen(weather_api).read())
        weather_today = weather['data']['forecast'][0]
        weather_tomorrow = weather['data']['forecast'][1]
        content = ('今天是 {today_date}\n'
                   '天气{today_type}\n'
                   '{today_sunrise}日出，{today_sunset}日落\n'
                   '{today_low},{today_high}\n'
                   '{today_fx} {today_fl}\n'
                   '{today_notice}\n\n'
                   '明天是 {tomorrow_date}\n'
                   '天气{tomorrow_type}\n'
                   '{tomorrow_sunrise}日出，{tomorrow_sunset}日落\n'
                   '{tomorrow_low},{tomorrow_high}\n'
                   '{tomorrow_fx} {tomorrow_fl}\n'
                   '{tomorrow_notice}\n')

        return content.format(
            today_date=weather_today['date'],
            today_type=weather_today['type'],
            today_sunrise=weather_today['sunrise'],
            today_sunset=weather_today['sunset'],
            today_low=weather_today['low'],
            today_high=weather_today['high'],
            today_fx=weather_today['fx'],
            today_fl=weather_today['fl'],
            today_notice=weather_today['notice'],
            tomorrow_date=weather_tomorrow['date'],
            tomorrow_type=weather_tomorrow['type'],
            tomorrow_sunrise=weather_tomorrow['sunrise'],
            tomorrow_sunset=weather_tomorrow['sunset'],
            tomorrow_low=weather_tomorrow['low'],
            tomorrow_high=weather_tomorrow['high'],
            tomorrow_fx=weather_tomorrow['fx'],
            tomorrow_fl=weather_tomorrow['fl'],
            tomorrow_notice=weather_tomorrow['notice'],
        )
    except:
        print('这API又出问题了。。。')
        return '这API又出问题了。。。'


def send_mail(sender, pwd, receiver, subject, content):
    message = MIMEText(content)
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receiver
    smtpserver = 'smtp.qq.com'
    try:
        s = smtplib.SMTP_SSL(smtpserver, 465)
        s.login(sender, pwd)
        s.sendmail(sender, receiver, message.as_string())
        print('邮件发送成功')
    except Exception as e:
        print('Error:无法发送邮件.Case:%s' % e)
    finally:
        s.quit()


def main():
    sender = ''  #自己的qq邮箱
    pwd = ''  #授权码
    receiver = ''  #对方邮箱
    subject = '天气预报'
    content = get_weather_info('杭州')

    send_mail(sender, pwd, receiver, subject, content)


if __name__ == '__main__':
    main()
