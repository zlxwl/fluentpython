# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 下午4:03
# @Author  : Zhong Lei
# @FileName: bulkfood_v7.py
import sys
sys.path.append('.')
import chapter20.model_v5 as model


class LineItem(model.Entity):
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price


if __name__ == '__main__':
    item = LineItem('apple', 50, 100.0)
    print(item.weight)
