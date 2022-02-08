# -*- coding: utf-8 -*-
# @Time    : 2022/1/10 上午8:54
# @Author  : Zhong Lei
# @FileName: corutine.py


def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received x:', x)


# === 16.2 使用协成产出两个值 ===
def simple_coro2(a):
    print('-> started a = ', a)
    b = yield a
    print('-> started b = ', b)
    c = yield b + a
    print('-> started c = ', c)


# === 16.4 预缴协成装饰器 ===
from functools import wraps


def coroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer


# === 16.3 使用协成计算移动平均值===
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


# === 16.7 yield from 关键字 ===
def gen():
    for c in 'ABC':
        yield c
    for i in range(1, 3):
        yield i


def gen_1():
    yield from 'ABC'
    yield from range(1, 3)


# === 16-16 ===
def chain(*iterables):
    for it in iterables:
        yield from it


if __name__ == '__main__':
    # 16-1
    # my_coro = simple_coroutine()
    # print(my_coro)
    # next(my_coro)
    # my_coro.send(44)
    # print(my_coro)

    # 16-2
    # mycoro = simple_coro2(14)
    # from inspect import getgeneratorstate
    # print(getgeneratorstate(mycoro))
    #
    # next(mycoro)
    # print(getgeneratorstate(mycoro))
    #
    # mycoro.send(28)
    # print(getgeneratorstate(mycoro))
    #
    # mycoro.send(99)
    # print(getgeneratorstate(mycoro))

    # 16-3
    # coro_aveg = average()
    # next(coro_aveg)
    # print(coro_aveg.send(10))
    # print(coro_aveg.send(20))
    # print(coro_aveg.send(30))

    # 16-4 预缴装饰器
    # coro_aveg = average()
    # print(coro_aveg.send(10))
    # print(coro_aveg.send(20))
    # print(coro_aveg.send(30))

    # 16.7
    # import itertools
    # print(list(gen()))
    # print(list(gen_1()))
    # print(list(itertools.chain(range(1, 3), 'abc')))

    # 16-16
    print(list(chain(range(1, 3), 'abc')))