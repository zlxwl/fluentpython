# -*- coding: utf-8 -*-
# @Time    : 2022/1/17 下午3:06
# @Author  : Zhong Lei
# @FileName: bulkfood_v2.py


class LineItem:
    def __init__(self, description, price, weight):
        self.description = description
        self.price = price
        self.weight = weight

    def subtotal(self):
        return self.price * self.weight

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('value must be > 0')


if __name__ == '__main__':
    raisings = LineItem('apple', 10, 10)
    print(raisings.subtotal())
    raisings = LineItem('banana', 10, -10)

