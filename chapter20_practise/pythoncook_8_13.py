# -*- coding: utf-8 -*-
# @Time    : 2022/4/28 下午5:15
# @Author  : Zhong Lei
# @FileName: pythoncook_8_13.py


class Descriptor:
    def __init__(self, name=None, **kwargs):
        self.name = name
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        if instance is None:
            return self
        else:
            instance.__dict__[self.name] = value


class Typed(Descriptor):
    expect_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expect_type):
            raise TypeError('expected value {}'.format(self.expect_type))
        else:
            super().__set__(instance, value)


class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value > 0:
            super().__set__(instance, value)
        else:
            raise ValueError('value must be >0')


class MaxSized(Descriptor):
    def __init__(self, name=None, **kwargs):
        if 'size' not in kwargs:
            raise TypeError('size must be in name')
        super().__init__(name, **kwargs)

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('name size must be <0')
        super().__set__(instance, value)


class Integer(Typed):
    expect_type = int


class UnsignedInteger(Integer, Unsigned):
    pass


class Float(Typed):
    expect_type = float


class UnsignedFloat(Float, Unsigned):
    pass


class String(Typed):
    expect_type = str


class MaxSizedString(String, MaxSized):
    pass


class Stock:
    name = MaxSizedString('name', size=8)
    shares = UnsignedInteger('shares')
    price = UnsignedFloat('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


if __name__ == '__main__':
    s = Stock('apple', 50, 100.0)
    s.name = 'aaaaaaaaaaaaaaaaa'
