# -*- coding: utf-8 -*-
# @Time    : 2021/12/28 下午3:58
# @Author  : Zhong Lei
# @FileName: clockdeco2.py
import time
import functools


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_list = []
        if args:
            arg_list.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' %(k, w) for k, w in sorted(kwargs.items())]
            arg_list.append(', '.join(pairs))
        arg_str = ', '.join(arg_list)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n <2 else n*factorial(n-1)


if __name__ == '__main__':
    print('*'*40, 'Calling snooze(.123)')
    snooze(.123)
    print('*'*40, 'Calling factorial(6)')
    print('!6 =', factorial(6))
