# -*- coding: utf-8 -*-
# @Time    : 2022/4/26 下午2:21
# @Author  : Zhong Lei
# @FileName: lineitem_v4_prop.py


def quantity():
    try:
        quantity.counter += 1
    except:
        quantity.counter = 0

    storage_name = '_quantity#{}'.format(quantity.counter)

    def qty_get(instance):
        return getattr(instance, storage_name)

    def qty_set(instance, value):
        if value > 0:
            setattr(instance, storage_name, value)
        else:
            raise ValueError('value must be > 0')

    return property(fget=qty_get, fset=qty_set)


class LineItem:
    weight = quantity()
    price = quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def sub_total(self):
        return self.weight * self.price


if __name__ == '__main__':
    item = LineItem('apple', 15, 20.0)
    print(item.price)
    print(item.weight)
    print(item.sub_total())