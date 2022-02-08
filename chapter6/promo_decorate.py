# -*- coding: utf-8 -*-
# @Time    : 2021/12/28 上午11:55
# @Author  : Zhong Lei
# @FileName: promo_decorate.py
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
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


promos = []


def promotion(func):
    promos.append(func)
    return func


def best_promo(order):
    return max(promo(order) for promo in promos)


@promotion
def fidelity_promo(self) -> float:
    return self.total() * 0.05 if self.customer[1] > 1000 else 0


@promotion
def bulk_item_promo(self):
    discount = 0
    for item in self.cart:
        if item.quality > 20:
            discount += 0.1 * item.quality * item.price
    return discount

@promotion
def large_order_promo(self):
    products = [item.product for item in self.cart]
    return self.total() * 0.07 if len(products) >= 10 else 0


cart = [
    LineItem('banana', 4, 0.5),
    LineItem('apple', 10, 1.5),
    LineItem('watermello', 5, 5.0)
]

print(Order(joe, cart, fidelity_promo))
print(Order(ann, cart, fidelity_promo))

banana_cart = [
    LineItem('banana', 30, 0.5),
    LineItem('apple', 10, 1.5)
]
print(Order(joe, banana_cart, bulk_item_promo))

long_order = [
    LineItem(str(item_code), 1, 1.0) for item_code in range(10)
]
print(Order(joe, long_order, large_order_promo))
print(Order(joe, cart, large_order_promo))

print(Order(joe, long_order, best_promo))
print(Order(joe, banana_cart, best_promo))
print(Order(ann, cart, best_promo))