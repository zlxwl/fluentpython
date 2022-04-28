# -*- coding: utf-8 -*-
# @Time    : 2022/4/28 下午4:37
# @Author  : Zhong Lei
# @FileName: pythoncook_8_13.py
import math


class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            # bounded_method = self.func.__get__(instance) == instance.square
            # value = self.func.__get__(instance).__call__()
            value = self.func(instance)
            setattr(instance, self.name, value)
            return value


# def lazyproperty(func):
#     name = '_lazy' + func.__name__
#
#     @property
#     def wrapper(self):
#         if hasattr(self, name):
#             return getattr(self, name)
#         else:
#             value = func(self)
#             setattr(self, name, value)
#         return value
#
#     return wrapper


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def square(self):
        print('computing')
        return self.radius * (math.pi ** 2)


if __name__ == '__main__':
    c = Circle(5)
    print(c.square)
    print(c.__dict__)
    print(c.square)
    print(c.__dict__)
