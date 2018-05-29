# -*- coding: utf-8 -*-
import urllib.request
import json
import datetime
import os


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


def download(id_list, num):
    dt = datetime.datetime.now()
    path = dt.strftime('%Y-%m-%d')
    i = 0
    while os.path.exists(path):
        path = path + '_' + str(i)
        i += 1
    os.mkdir(path)

    url_music_list = 'http://music.163.com/api/playlist/detail?id={id}'
    url_music_link = 'http://music.163.com/song/media/outer/url?id={id_music}.mp3'

    r = urllib.request.urlopen(
        url_music_list.format(id=id_list)).read().decode(
            'utf-8', errors='ignore')
    arr = json.loads(r)['result']['tracks']

    for i in range(num):
        try:
            name = arr[i]['name'] + '.mp3'
            id_music = arr[i]['id']
            link = url_music_link.format(id_music=id_music)
            urllib.request.urlretrieve(link, path + '/' + name)
            print(name + '下载完成')
        except:
            pass


def main():
    #云音乐飙升榜
    id_1 = '19723756'
    #云音乐新歌榜
    id_2 = '3779629'
    #网易原创歌曲榜
    id_3 = '2884035'
    #云音乐热歌榜
    id_4 = '3778678'

    id_lis = [id_1, id_2, id_3, id_4]

    print('云音乐飙升榜 ------ 1')
    print('云音乐新歌榜 ------ 2')
    print('网易原创歌曲榜 ------ 3')
    print('云音乐热歌榜 ------ 4')
    t = int(input('请选择下载的歌曲榜单（1-4）：'))
    num = int(input('请选择下载个歌曲数量（1-100）：'))
    id_list = id_lis[t - 1]

    pretend()
    download(id_list, num)
    print('Done!')


if __name__ == "__main__":
    main()