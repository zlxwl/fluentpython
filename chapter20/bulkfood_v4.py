# -*- coding: utf-8 -*-
# @Time    : 2022/1/18 下午2:54
# @Author  : Zhong Lei
# @FileName: bulkfood_v4.py


class Quantity:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        name = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(name, index)
        cls.__counter += 1

    def __get__(self, instance, owner):
        return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError('value must be > 0')


class LineItem:
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.weight = weight
        self.price = price
        self.description = description

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    print(LineItem('apple', 10, 10).subtotal())
    banana = LineItem('banana', 1, 10)
    print(banana.weight, banana.price)
    print(getattr(banana, '_Quantity#0'))
    print(getattr(banana, '_Quantity#1'))
