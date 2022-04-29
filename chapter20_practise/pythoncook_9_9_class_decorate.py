# -*- coding: utf-8 -*-
# @Time    : 2022/4/29 下午5:36
# @Author  : Zhong Lei
# @FileName: pythoncook_9_9_class_decorate.py
import types
from functools import wraps


class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncall = 0

    def __call__(self, *args, **kwargs):
        self.ncall += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


@Profiled
def add(x, y):
    return x + y


class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)


def grok(self, x):
    pass


if __name__ == '__main__':
    # a = add(10, 20)
    # print(add.ncall)
    # add(12, 12)
    # print(add.ncall)
    s = Spam()
    print(Spam.bar.__get__(s, Spam)(2))
    s.bar(3)
    print(grok.__get__(s, Spam))
