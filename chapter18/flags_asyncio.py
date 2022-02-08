# -*- coding: utf-8 -*-
# @Time    : 2022/1/13 下午6:05
# @Author  : Zhong Lei
# @FileName: flags_asyncio.py
import asyncio
import aiohttp

from chapter17.flags import BASE_URL, save_flag, show, main, POP20_CC


@asyncio.coroutine
def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = yield from aiohttp.ClientSession().get(url)
    img = yield from resp.read()
    return img


@asyncio.coroutine
def download_one(cc):
    img = yield from get_flag(cc)
    show(cc)
    save_flag(img, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    loop = asyncio.get_event_loop()
    to_do = [download_one(cc) for cc in cc_list]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()
    return len(res)


if __name__ == '__main__':
    main(download_many)