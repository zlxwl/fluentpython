# -*- coding: utf-8 -*-
# @Time    : 2022/1/10 上午11:06
# @Author  : Zhong Lei
# @FileName: coaverage.py
from chapter16.corutine import coroutine


@coroutine
def average():
    total = 0
    count = 0
    average = None
    while True:
        term = yield average
        count += 1
        total += term
        average = total/count


if __name__ == '__main__':
    coro_aveg = average()
    print(coro_aveg.send(10))
    print(coro_aveg.send(20))
    print(coro_aveg.send(30))