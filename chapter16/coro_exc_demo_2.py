# -*- coding: utf-8 -*-
# @Time    : 2022/1/10 上午11:40
# @Author  : Zhong Lei
# @FileName: coro_exc_demo_2.py


class DemoException:
    pass


def coro_demo_handling():
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('handling demo exception')
            else:
                print('received x: {}'.format(x))
    finally:
        print('-> coroutine ended!')


if __name__ == '__main__':
    coro = coro_demo_handling()
    next(coro)
    coro.throw(ZeroDivisionError)