# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 上午11:46
# @Author  : Zhong Lei
# @FileName: bulk_food_v6.py
from chapter20.model_v5 import *


@entity
class LineItem:
    description = NonBlank()
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price


if __name__ == '__main__':
    line = LineItem('apple', 50, 10.0)
    print(dir(line))
    print(getattr(line, '_NonBlank#description'))
    print(LineItem.description.storage_name)