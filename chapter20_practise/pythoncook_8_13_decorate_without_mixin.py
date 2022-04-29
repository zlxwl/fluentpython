# -*- coding: utf-8 -*-
# @Time    : 2022/4/29 下午3:50
# @Author  : Zhong Lei
# @FileName: pythoncook_8_13_decorate_without_mixin.py
from functools import partial


def Typed(expected_type, cls=None):
    if cls is None:
        return lambda cls: Typed(expected_type, cls)

    temp_set = cls.__set__

    def __set__(self, instance, value):
        if not isinstance(value, expected_type):
            raise TypeError('expected {}'.format(expected_type))
        temp_set(self, instance, value)
    cls.__set__ = __set__
    return cls


def Unsigned(cls):
    temp_set = cls.__set__

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('value must be >0')
        temp_set(self, instance, value)

    cls.__set__ = __set__
    return cls


def MaxSized(cls):
    temp_init = cls.__init__

    def __init__(self, name=None, **kwargs):
        if 'size' not in kwargs:
            raise TypeError('missed size')
        temp_init(self, name, **kwargs)

    cls.__init__ = __init__

    temp_set = cls.__set__

    def __set__(self, instance, value):
        if len(value) > self.size:
            raise ValueError('value must be < {}'.format(self.size))
        temp_set(self, instance, value)

    cls.__set__ = __set__
    return cls


@Typed(float)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


@MaxSized
class Person:
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    p = Person('apple')