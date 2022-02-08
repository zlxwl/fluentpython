# -*- coding: utf-8 -*-
# @Time    : 2022/1/14 下午4:31
# @Author  : Zhong Lei
# @FileName: flag_get.py
import asyncio
import aiohttp


@asyncio.coroutine
def run():
    res = yield from aiohttp.ClientSession().get('http://flupy.org/data/flags/cn/metadata.json')
    if res.status == 200:
        ctype = res.headers.get('Content-type', '').lower()
        if 'json' in ctype:
            data = yield from res.json()
    return data


def drive(run):
    loop = asyncio.get_event_loop()
    coro = asyncio.ensure_future(run())
    res = loop.run_until_complete(coro)
    loop.close()
    return res


if __name__ == '__main__':
    print(drive(run)['country'])