# -*- coding: utf-8 -*-
# @Time    : 2022/1/10 上午11:45
# @Author  : Zhong Lei
# @FileName: coaverage2.py
from collections import namedtuple

Result = namedtuple('Result', 'count average')


def average():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average)


if __name__ == '__main__':
    average_demo = average()
    next(average_demo)

    # average_demo.send(10)
    # average_demo.send(25)
    # average_demo.send(None)

    average_demo.send(10)
    average_demo.send(30)
    try:
        average_demo.send(None)
    except Exception as exc:
        result = exc.value
    print(result[0])