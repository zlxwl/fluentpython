# -*- coding: utf-8 -*-
# @Time    : 2021/12/30 下午2:42
# @Author  : Zhong Lei
# @FileName: vector2d_v3.py
import math
from array import array


class Vector2d:
    # __slots__ = ('__x', '__y')
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

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
    v1 = Vector2d(3, 4)
    v2 = Vector2d(3.1, 4.1)
    print(hash(v1))
    print(hash(v2))
    print(set([v1, v2]))
    print(v1._Vector2d__x)
    print(v1.__dict__)