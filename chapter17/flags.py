# -*- coding: utf-8 -*-
# @Time    : 2022/1/12 上午10:48
# @Author  : Zhong Lei
# @FileName: flags.py
import os
import time
import sys

import requests


POP20_CC = ('CN', 'IN', 'US', 'ID', 'BR', 'PK', 'NG', 'BD', 'RU', 'JP', 'MX', 'PH', 'VN', 'ET', 'DE', 'IR', 'CD', 'FR')
BASE_URL = 'http://flupy.org/data/flags'
DEST_DIR = 'downloads'


def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)
    with open(path, 'wb') as f:
        f.write(img)


def get_flag(cc: str):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp.content


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


def download_many(cc_list):
    for cc in cc_list:
        img = get_flag(cc)
        show(cc)
        save_flag(img, cc.lower() + '.gif')
    return len(cc_list)


def main(download_many):
    t0 = time.time()
    count = download_many(POP20_CC)
    elapsed = time.time() - t0
    msg = '\n{} flags download in {:.2f}s'
    print(msg.format(count, elapsed))


if __name__ == '__main__':
    main(download_many)