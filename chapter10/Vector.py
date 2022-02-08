# -*- coding: utf-8 -*-
# @Time    : 2021/12/31 上午10:55
# @Author  : Zhong Lei
# @FileName: Vector.py
from array import array
import reprlib
import math
import numbers


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

    def __bytes__(self):
        return (
            bytes([ord(self.typecode)])
            + bytes(self._components)
        )

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(x*x for x in self._components)

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(self._components[item])
        elif isinstance(item, numbers.Integral):
            return self._components[item]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_name.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__} object has no attribute {!r}'
        return msg.format(cls, name)

    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1:
            if name in self.shortcut_name:
                error = 'read only attribute {attr_name !r}'
            elif name.islower():
                error = 'can not set attribute a to z in {cls_name !r}'
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super(Vector, self).__setattr__(name, value)

    @classmethod
    def from_bytes(cls, octets):
        typecode = octets[0]
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)


if __name__ == '__main__':
    # print(Vector([3.1, 4.1]).__repr__())
    # print(Vector((3, 4, 5)))
    # print(Vector(range(10)).__repr__())
    # print(len(Vector(range(10))))
    # print(Vector(range(10))[5])

    v = Vector(range(7))
    print(v)
    print(v.__repr__())
    # print(v.x)
    # v.x = 10
    # print(v.x)
    # print(v)
