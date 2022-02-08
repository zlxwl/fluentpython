# -*- coding: utf-8 -*-
# @Time    : 2021/12/30 上午11:16
# @Author  : Zhong Lei
# @FileName: vector2d_v0.py
import math
from array import array


class Vector2:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __eq__(self, other):
        # return self.x == other.x and other.y == self.y
        return tuple(self) == tuple(self)

    def __abs__(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __bool__(self):
        return bool(abs(self))

    def __bytes__(self):
        return (
                    bytes([ord(self.typecode)])
                    + bytes(array(self.typecode, self))
        )

    def angle(self):
        return math.atan2(self.y, self.x)

    # def __format__(self, format_spec):
    #     commpoents = (format(c, format_spec) for c in self)
    #     return '({}, {})'.format(*commpoents)
    def __format__(self, format_spec: str = ''):
        if format_spec.endswith('p'):
            format_spec = format_spec[:-1]
            cords = (self.__abs__(), self.angle())
            fmt_str = "<{}, {}>"
        else:
            cords = self
            fmt_str = '({}, {})'
        components = (format(c, format_spec) for c in cords)
        return fmt_str.format(*components)

    @classmethod
    def from_bytes(cls, octets):
        typecode = chr(octets[0])
        mevw = memoryview(octets[1:]).cast(typecode)
        return cls(*mevw)


if __name__ == '__main__':
    v1 = Vector(3, 4)
    print(v1.x, v1.y)

    x, y = v1
    print(x, y)

    v1 = Vector(3.0, 4.0)
    v1_clone = eval(repr(v1))
    print(v1 == v1_clone)

    octets = bytes(v1)
    print(octets)
    print(abs(v1))
    print(bool(v1), bool(Vector(0, 0)))

    print(Vector.from_bytes(octets))

    # 格式输出
    print(format(v1, '.2p'))