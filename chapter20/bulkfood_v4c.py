# -*- coding: utf-8 -*-
# @Time    : 2022/1/18 下午3:33
# @Author  : Zhong Lei
# @FileName: bulkfood_v4c.py
import chapter20.models_v4c as model


class LineItem:
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.price * self.weight


if __name__ == '__main__':
    apple = LineItem('apple', 10, 10)
    print(apple.subtotal())
    print(apple.weight)