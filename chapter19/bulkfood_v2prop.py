# -*- coding: utf-8 -*-
# @Time    : 2022/1/17 下午3:56
# @Author  : Zhong Lei
# @FileName: bulkfood_v2prop.py


def quantity(storage_name):
    def qty_getter(instance):
        return instance.__dict__[storage_name]

    def qty_setter(instance, value):
        if value > 0:
            instance.__dict__[storage_name] = value
        else:
            raise ValueError('value must be > 0')

    return property(qty_getter, qty_setter)


class LineItem:
    weight = quantity('weight')
    price = quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.price * self.weight


if __name__ == '__main__':
    nutmeg = LineItem('Moluccan nutmeg', 8, 13.95)
    nutmeg.weight, nutmeg.price = (8, 13.95)

    print(sorted(vars(nutmeg).items()))