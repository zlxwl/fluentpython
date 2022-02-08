# -*- coding: utf-8 -*-
# @Time    : 2022/1/5 下午3:56
# @Author  : Zhong Lei
# @FileName: vector_v6.py
import reprlib
import math
import random
from array import array
import numbers
import itertools


class Vector:
    typecode = 'd'
    shortcut_name = 'xyzt'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __eq__(self, other):
        if isinstance(other, Vector):
            return (len(self) == len(other) and
                    any(x == y for x in self for y in other))
        # return tuple(self) == tuple(other)
        else:
            raise NotImplemented

    def __len__(self):
        return len(self._components)

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(self._components[item])
        elif isinstance(item, numbers.Integral):
            return self._components[item]
        else:
            msg = '{cls.__name__ must be integers}'
            raise TypeError(msg.format(cls=cls))

    def __getattr__(self, item):
        cls = type(self)
        if len(item) == 1:
            pos = cls.shortcut_name.find(item)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__} object has no attribute {!r}'
        return msg.format(cls, item)

    def __setattr__(self, key: str, value):
        cls = type(self)
        if len(key) == 1:
            if key in self.shortcut_name:
                error = 'read only attribute {attr_name !r}'
            elif key.islower():
                error = 'can not set attribute a to z in {cls_name !r}'
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=key)
                raise AttributeError(msg)
        super(Vector, self).__setattr__(key, value)

    def __abs__(self):
        return math.sqrt(x*x for x in self._components)

    def __bool__(self):
        return bool(abs(self))

    def __bytes__(self):
        return (
            bytes([ord(self.typecode)]) +
            bytes(self._components)
        )

    def __neg__(self):
        return Vector(-x for x in self._components)

    def __pos__(self):
        return Vector(self)

    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0)
            return Vector(x + y for x, y in pairs)
        except TypeError:
            raise NotImplemented

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, numbers.Real):
            return Vector(n*other for n in self)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __matmul__(self, other):
        try:
            return sum(x * y for x, y in zip(self, other))
        except TypeError:
            raise NotImplemented

    def __rmatmul__(self, other):
        return other * self

    @classmethod
    def from_bytes(cls, octets):
        typecode = octets[0]
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


if __name__ == '__main__':
    v = Vector(range(4))
    print(v)
    print(v.__repr__())
    print((-v).__repr__())
    v1 = Vector([3, 4, 5])
    print(v1 + (10, 20, 30))
    from chapter9.vector2d_v0 import Vector2
    v2 = Vector2(1, 2)
    print(v1 + v2)
    print(v2 + v1)
    # print(1 + v2)

    print(11*v)
    # print(v*v1)

    v3 = Vector(range(4))
    print(v @ v3)

    va = Vector([1.0, 2.0, 3.0])
    vb = Vector(range(1, 4))
    print(va == vb)

    vc = Vector([1, 2])
    # print(vc == v2)

    # t3 = (1, 2, 3)
    # print(va == t3)
    v = Vector([1, 2, 3])
    v_alias = v
    print(id(v))
    print(v)
    v += Vector([4, 5, 6])
    print(id(v))
    print(v)
    print(v_alias)
