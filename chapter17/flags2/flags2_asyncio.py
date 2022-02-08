# -*- coding: utf-8 -*-
# @Time    : 2022/1/14 上午10:03
# @Author  : Zhong Lei
# @FileName: flags2_asyncio.py
import asyncio
import collections
import sys

import aiohttp
from aiohttp import web
import tqdm

from chapter17.flags2.flags2_commons import main, HTTPStatus, \
    Result, save_flags

DEFAULT_CONCUR_REQ = 18
MAX_CONCUR_REQ = 1000


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


class FetchError(Exception):
    def __init__(self, country_code):
        self.country_code = country_code


@asyncio.coroutine
def get_flag(base_url, cc):
    url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
    resp = yield from aiohttp.ClientSession().get(url)
    if resp.status == 200:
        img = yield from resp.read()
        return img
    elif resp.status == 404:
        raise web.HTTPNotFound()
    else:
        raise aiohttp.HttpProcessingError(
            code=resp.status, message=resp.reason, headers=resp.headers
        )


@asyncio.coroutine
def download_one(cc, base_url, semaphore, verbose):
    try:
        with (yield from semaphore):
            img = yield from get_flag(base_url, cc)
    except web.HTTPNotFound:
        status = HTTPStatus.not_found
        msg = 'not_found'
    except Exception as exc:
        raise FetchError(cc) from exc
    else:
        # show(cc)
        # save_flags(img, cc.lower() + '.gif')
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, save_flags, img, cc.lower() + '.gif')
        msg = 'OK'
        status = HTTPStatus.ok
    if verbose:
        print(cc, msg)
    return Result(status, cc)


@asyncio.coroutine
def downloader_coro(cc_list, base_url, verbose, concur_req):
    counter = collections.Counter()
    semaphore = asyncio.Semaphore(concur_req)
    to_do = [download_one(cc, base_url, semaphore, verbose) for cc in cc_list]
    to_do_iter = asyncio.as_completed(to_do)

    if not verbose:
        to_do_iter = tqdm.tqdm(to_do_iter, total=len(cc_list))

    for future in to_do_iter:
        try:
            res = yield from future
        except FetchError as exc:
            country_code = exc.country_code
            try:
                error_msg = exc.__cause__.args[0]
            except IndexError:
                error_msg = exc.__cause__.__class__.__name__
            if verbose and error_msg:
                msg = '***Error for {}: {}'
                print(msg.format(country_code, error_msg))
            status = HTTPStatus.error
        else:
            status = res.status
        counter[status] += 1

    return counter


def download_many(cc_list, base_url, verbose, concur_req):
    loop = asyncio.get_event_loop()
    coro = downloader_coro(cc_list, base_url, verbose, concur_req)
    counts = loop.run_until_complete(coro)
    loop.close()
    return counts


if __name__ == '__main__':
    main(download_many, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ)