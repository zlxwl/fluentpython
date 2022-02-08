# -*- coding: utf-8 -*-
# @Time    : 2021/12/28 下午4:08
# @Author  : Zhong Lei
# @FileName: clockdeco.py
import time
import functools


# === 7.8 标准库中的装饰器 ===
def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        args_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, args_str, result))
        return result
    return clocked

@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    print(fibonacci(30))