# -*- coding: utf-8 -*-
# @Time    : 2021/12/27 下午3:58
# @Author  : Zhong Lei
# @FileName: 06-design-pattens.py

# === 6.1 重构策略模式 ===
# === 6.1.1 经典的策略模式 ===
from abc import ABC, abstractmethod
from collections import namedtuple
Customer = namedtuple('Customer','name fidelity')
joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)


class LineItem(object):
    def __init__(self, product, quality, price):
        self.product = product
        self.quality = quality
        self.price = price

    def total(self):
        return self.quality * self.price


class Order(object):
    def __init__(self, customer: Customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        return sum(item.total() for item in self.cart)

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):
    def discount(self) -> float:
        pass


class FidelityPromo(Promotion):
    def discount(self) -> float:
        # if self.customer[1] > 1000:
        #     discount = 0.05
        # else:
        #     return 0
        return self.total() * 0.05 if self.customer[1] > 1000 else 0


class BulkItemPromo(Promotion):
    def discount(self):
        discount = 0
        for item in self.cart:
            if item.quality > 20:
                discount += 0.1 * item.quality * item.price
        return discount


class LargeOrderPromo(Promotion):
    def discount(self):
        products = [item.product for item in self.cart]
        return self.total() * 0.07 if len(products) >= 10 else 0


cart = [
    LineItem('banana', 4, 0.5),
    LineItem('apple', 10, 1.5),
    LineItem('watermello', 5, 5.0)
]

print(Order(joe, cart, FidelityPromo))
print(Order(ann, cart, FidelityPromo))

banana_cart = [
    LineItem('banana', 30, 0.5),
    LineItem('apple', 10, 1.5)
]
print(Order(joe, banana_cart, BulkItemPromo))

long_order = [
    LineItem(str(item_code), 1, 1.0) for item_code in range(10)
]
print(Order(joe, long_order, LargeOrderPromo))
print(Order(joe, cart, LargeOrderPromo))
