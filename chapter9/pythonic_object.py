# -*- coding: utf-8 -*-
# @Time    : 2021/12/29 下午4:58
# @Author  : Zhong Lei
# @FileName: pythonic_object.py


# === 9.4 classmethod 和 staticmethod方法的区别 ===
class Demo:
    @classmethod
    def klassmeth(cls, *args):
        return args

    @staticmethod
    def statmeth(*args):
        return args

print(Demo.klassmeth('aa'))
print(Demo.statmeth('aa'))


# === 9.9 覆盖类属性 ===
from chapter9.vector2d_v3 import Vector2d
v1 = Vector2d(1.1, 2.2)
dumped = bytes(v1)
print(dumped)
print(len(dumped))

v1.typecode = 'f'
dumpf = bytes(v1)
print(dumpf)
print(len(dumpf))

print(Vector2d.typecode)

from chapter9.vector2d_v3 import Vector2d
class ShortVector2d(Vector2d):
    typecode = 'f'


sv = ShortVector2d(1/11, 1/27)
print(sv)
print(len(bytes(sv)))