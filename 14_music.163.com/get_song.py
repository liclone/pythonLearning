# -*- coding: utf-8 -*-
'''
自定义下载网易云音乐
打开网易云音乐网页版，从url得到某音乐的id，以及其歌曲名
将id，歌曲名写入Songs.txt 格式为 id 空格 歌曲名
'''

import urllib.request
import os


# 歌曲保存路径
dir = r'D:\Music'
# Songs.txt 绝对路径
Song_txt = r'F:\Python\Misc\Songs.txt'
if not os.path.exists(dir):
    os.mkdir(dir)
os.chdir(dir)
url_music_link = 'http://music.163.com/song/media/outer/url?id={id_music}.mp3'


def download(id_music, name):
    print(name + '   downloading...')
    urllib.request.urlretrieve(url_music_link.format(id_music=id_music), name + '.mp3')
    print('Done')


def get_one_song():
    id_music = input('music id : ')
    name_music = input('music name : ')
    download(id_music, name_music)


def get_songs():
    with open(Song_txt, 'r', encoding='utf-8') as f:
        for song in f:
            info = song.split()
            if info:  # 防止空行
                id_music = ''
                for i in info[0]:  # 避免id处出现其他字符，
                   if i.isdigit():
                       id_music += i
                download(id_music, ' '.join(info[1:]))
    print('All Done!!!')


if __name__ == "__main__":
    get_songs()
