# -*- coding: utf-8 -*-
# @Time    : 2022/4/26 下午12:19
# @Author  : Zhong Lei
# @FileName: lineitem_v4.py


class Quantity:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        self.prefix = cls.__name__
        self.index = cls.__counter
        self.storage_name = '_{}#{}'.format(self.prefix, self.index)
        cls.__counter += 1

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError('value must be > 0')

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name)


class LineItem:
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def sub_total(self):
        return self.weight * self.price


if __name__ == '__main__':
    item = LineItem('apple', 15, 20.0)
    print(item.weight, item.price)
    print(item.sub_total())
    print(getattr(item, '_Quantity#0'))
    print(getattr(item, '_Quantity#1'))
    print(LineItem.weight)