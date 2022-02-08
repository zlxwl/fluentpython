# -*- coding: utf-8 -*-
# @Time    : 2022/1/13 下午3:38
# @Author  : Zhong Lei
# @FileName: asyncio_demo.py
# -*- coding: utf-8 -*-
# @Time    : 2022/1/13 下午2:59
# @Author  : Zhong Lei
# @FileName: spinner_asyncio.py
import asyncio
import itertools
import sys


async def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        staus = char + '' + msg
        write(staus)
        flush()
        write('\x08'*len(staus))
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    write(' ' * len(staus) + '\x08' * len(staus))


async def slow_function():
    await asyncio.sleep(3)
    return 42


async def supervisor():
    spinner = asyncio.ensure_future(spin('thinking!'))
    print('spinner object:', spinner)
    result = await slow_function()
    spinner.cancel()
    return result


def main():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(supervisor())
    loop.close()
    return result


if __name__ == '__main__':
    main()