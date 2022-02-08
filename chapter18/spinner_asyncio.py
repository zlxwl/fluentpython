# -*- coding: utf-8 -*-
# @Time    : 2022/1/13 下午2:59
# @Author  : Zhong Lei
# @FileName: spinner_asyncio.py
import asyncio
import itertools
import sys


@asyncio.coroutine
def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        staus = char + '' + msg
        write(staus)
        flush()
        write('\x08'*len(staus))
        try:
            yield from asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    write(' ' * len(staus) + '\x08' * len(staus))


@asyncio.coroutine
def slow_function():
    yield from asyncio.sleep(3)
    return 42


@asyncio.coroutine
def supervisor():
    spinner = asyncio.ensure_future(spin('thinking!'))
    print('spinner object:', spinner)
    result = yield from slow_function()
    spinner.cancel()
    return result


def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor())
    loop.close()
    print('Answer:', result)


if __name__ == '__main__':
    main()