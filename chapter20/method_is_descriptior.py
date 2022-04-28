# -*- coding: utf-8 -*-
# @Time    : 2022/1/19 下午5:53
# @Author  : Zhong Lei
# @FileName: method_is_descriptior.py


import collections


class Text(collections.UserString):
    def __repr__(self):
        return 'Text({!r})'.format(self.data)

    def reverse(self):
        return self[::-1]

#
# class TextCall:
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self, *args, **kwargs):
#         for arg in args:
#             self.text_call(arg)
#
#     def text_call(self, x):
#         print('call test_call'.format(x))


class Quantity:
    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        if value > 0:
            print('__set__ method setting {}: {}'.format(self.name, value))
            instance.__dict__[self.name] = value
        else:
            raise TypeError('value must be > 0')

    def __get__(self, instance, owner):
        print('using getting')
        if instance is None:
            return self
        else:
            print('__get__ method getting {}: {}'.format(self.name, instance.__dict__[self.name]))
            return instance.__dict__[self.name]


class LineItem:
    weight = Quantity('weight')
    price = Quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


def add(x, y):
    return x + y


if __name__ == '__main__':
    # word = Text('forward')
    # word2 = Text('abb')
    # print(word)
    # print(word.reverse())
    # print(Text.reverse(Text('backward')))
    # print(type(Text.reverse), type(word.reverse))
    # print(list(map(Text.reverse, ['rapid', (10, 20, 30), Text('reversed')])))
    # print(Text.reverse.__get__(word))
    # print(Text.reverse.__get__(None, word))
    # print(word.reverse)
    # print(word.reverse.__self__)
    # print(word.reverse.__func__ is Text.reverse)
    # print(word.reverse.__func__)
    # print(word.reverse.__func__.__call__(word.reverse.__self__))
    # print(Text.reverse.__get__(word).__call__())

    # Text.reverse.__get__(word) == word.reverse
    # bounded_method = Text.reverse.__get__(word)
    # print(word.reverse.__func__.__call__(word2.reverse.__self__))
    # print(Text.__dict__)
    # print(word.__dict__)
    # word.__dict__['add'] = add
    # result = word.add(10, 20)
    # print(result)
    # word.add = 0
    # print(word.add)
    #
    # Text.reverse = 6
    # print(word.reverse)

    # item = LineItem('apple', 16, 20)
    # item.weight
    # item.weight = 60
    # item.__dict__['weight'] = 80
    # item.weight = 20
    # item.weight
    # print(item.__dict__['weight'])

    # monkey pack
    # LineItem.weight = 7
    # item2 = LineItem('apple', 12, 30)
    # print(item2.description)
    # print(item2.weight)
    # print(item2.price)
    #
    # no __get__
    # item = LineItem('apple', 10, 15)
    # item.weight = 20
    # item.weight
    # item.__dict__['weight'] = 'aa'
    # item.weight

    # no __set__
    item = LineItem('apple', 10, 15)
    item.price = 55
    item.price
    item.__dict__['price'] = 100
    item.price

