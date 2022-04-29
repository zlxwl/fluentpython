# -*- coding: utf-8 -*-
# @Time    : 2022/4/29 下午4:59
# @Author  : Zhong Lei
# @FileName: pythoncook_8_9_decorate_descriptor.py


class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected = expected_type

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected):
            raise TypeError('expected {}'.format(self.expected))

    def __delete__(self, instance):
        del instance.__dict__[self.name]


def type_assert(**kwargs):
    def wrapper(cls):
        for name, expected in kwargs.items():
            setattr(cls, name, Typed(name, expected))
        return cls
    return wrapper


@type_assert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('value must be int')
        else:
            instance.__dict__[self.name] = value


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    # s = Stock('apple', 100, 50.0)
    p = Point(2, 3)
    print(Point.x.__get__(p, Point))
    print(Point.x)
    print(p)