# -*- coding: utf-8 -*-
# @Time    : 2022/1/7 下午2:44
# @Author  : Zhong Lei
# @FileName: mirror_gen.py
import contextlib
import sys


@contextlib.contextmanager
def looking_glass():
    # __enter__()
    origin_write = sys.stdout.write

    def reverse_write(text):
        return origin_write(text[::-1])
    sys.stdout.write = reverse_write
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:
        msg = 'please do not divide by zero'
    # __exit__()
    finally:
        sys.stdout.write = origin_write
        if msg:
            print(msg)
        # sys.stdout.write = origin_write


if __name__ == '__main__':
    with looking_glass() as what:
        print(1/0)
        print(what)

    print(what)
    print('aaa')