# -*- coding: utf-8 -*-
# @Time    : 2022/1/18 下午3:15
# @Author  : Zhong Lei
# @FileName: bulkfoot_v4b.py


class Quantity:
    __counter = 0

    def __init__(self):
        name = self.__class__.__name__
        self.storage_name = '_{}#{}'.format(name, self.__counter)
        self.__counter += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
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
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.price * self.weight


if __name__ == '__main__':
    # apple = LineItem('apple', 10, 10)
    # print(apple.subtotal())
    print(LineItem.weight)
