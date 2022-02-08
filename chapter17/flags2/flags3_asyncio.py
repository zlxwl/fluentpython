# -*- coding: utf-8 -*-
# @Time    : 2022/1/14 下午3:45
# @Author  : Zhong Lei
# @FileName: flags3_asyncio.py
import tqdm
import collections
import asyncio
import aiohttp
from aiohttp import web
from chapter17.flags2.flags2_commons import main, HTTPStatus, save_flags, Result, DEFAULT_CONCUR_REQ, MAX_CONCUR_REQ
from chapter17.flags2.flags2_asyncio import FetchError


@asyncio.coroutine
def http_get(url):
    res = yield from aiohttp.ClientSession().get(url)
    if res.status == 200:
        ctype = res.headers.get('Content-type', '').lower()
        if 'json' in ctype or url.endswith('json'):
            data = yield from res.json()
        else:
            data = yield from res.read()
        return data

    elif res.status == 404:
        raise web.HTTPNotFound()
    else:
        raise aiohttp.error.HttpProcessingError(
            code=res.status, message=res.reason, header=res.headers
        )


@asyncio.coroutine
def get_country(base_url, cc):
    url = '{}/{cc}/metadata.json'.format(base_url, cc=cc.lower())
    metadata = yield from http_get(url)
    return metadata['country']


@asyncio.coroutine
def get_flag(base_url, cc):
    url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
    return (yield from http_get(url))


@asyncio.coroutine
def download_one(cc, base_url, semaphore, verbose):
    try:
        with (yield from semaphore):
            country = yield from get_country(base_url, cc)
        with (yield from semaphore):
            img = yield from get_flag(base_url, cc)
    except web.HTTPNotFound:
        status = HTTPStatus.not_found
        msg = 'not found'
    except Exception as exc:
        raise FetchError(cc) from exc
    else:
        country = country.replace(' ', '_')
        filename = '{}-{}.gif'.format(country, cc)
        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, save_flags, img, filename)

        # loop = asyncio.get_event_loop()
        # loop.run_in_executor(None, save_flags, img, cc.lower() + '.gif')
        status = HTTPStatus.ok
        msg = 'OK'
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