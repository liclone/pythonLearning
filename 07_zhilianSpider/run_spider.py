# -*-coding:utf-8-*-
from scrapy import cmdline
import os
from get_url import get_url


def main():
    if not os.path.exists('url_city.txt'):
        get_url()
    cmdline.execute('scrapy crawl zhilian --nolog'.split())


if __name__ == '__main__':
    main()
