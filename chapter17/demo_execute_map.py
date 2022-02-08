# -*- coding: utf-8 -*-
# @Time    : 2022/1/12 下午2:25
# @Author  : Zhong Lei
# @FileName: demo_execute_map.py
from time import sleep, strftime
from concurrent import futures


def display(*args):
    print(strftime('[%H:%M:%S]'), end=' ')
    print(*args)


def loiter(n):
    msg = '{}loiter({}): doing nothing for {}s ...'
    display(msg.format('\t'*n, n, n))
    sleep(n)

    msg = '{}loiter({}): done.'
    display(msg.format('\t'*n, n))
    return n * 10


def main():
    display('Script starting')
    executor = futures.ThreadPoolExecutor(max_workers=3)
    results = executor.map(loiter, range(5))
    display('results:', results)
    display('waiting for individual results:')
    for i, result in enumerate(results):
        display('results {}: {}'.format(i, result))


if __name__ == '__main__':
    main()