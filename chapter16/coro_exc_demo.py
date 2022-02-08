# -*- coding: utf-8 -*-
# @Time    : 2022/1/10 上午11:19
# @Author  : Zhong Lei
# @FileName: coro_exc_demo.py


class DemoException(Exception):
    pass


def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('demo exception handling ...')
        else:
            print('-> coroutine received: {!r}'.format(x))
    raise RuntimeError('This line should never run.')


if __name__ == '__main__':
    from inspect import getgeneratorstate
    # 16-9
    # exc_demo = demo_exc_handling()
    # next(exc_demo)
    # exc_demo.send(11)
    # exc_demo.send(22)
    # exc_demo.close()
    # print(getgeneratorstate(exc_demo))

    # 16-10
    # exc_demo = demo_exc_handling()
    # next(exc_demo)
    # exc_demo.send(11)
    # exc_demo.throw(DemoException)
    # print(getgeneratorstate(exc_demo))

    # 16-10
    exc_demo = demo_exc_handling()
    next(exc_demo)
    exc_demo.send(11)
    exc_demo.throw(ZeroDivisionError)
    print(getgeneratorstate(exc_demo))