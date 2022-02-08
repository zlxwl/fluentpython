# -*- coding: utf-8 -*-
# @Time    : 2022/1/18 下午7:10
# @Author  : Zhong Lei
# @FileName: bulkfood_v5.py

import chapter20.model_v5 as model


class LineItem:
    weight = model.Quantity()
    price = model.Quantity()
    description = model.NonBlank()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.price * self.weight


if __name__ == '__main__':
    apple = LineItem('apple', 10, 10)
    print(apple.weight)
    print(apple.subtotal())
    apple = LineItem('', 10, 10)
