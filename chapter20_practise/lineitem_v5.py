# -*- coding: utf-8 -*-
# @Time    : 2022/4/26 下午2:37
# @Author  : Zhong Lei
# @FileName: lineitem_v5.py
import abc


class AutoStorage:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix, index)
        cls.__counter += 1

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name)


class Validate(abc.ABC, AutoStorage):
    def __set__(self, instance, value):
        value = self.validate(instance, value)
        super().__set__(instance, value)

    @abc.abstractmethod
    def validate(self, instance, value):
        pass


class NoBlank(Validate):
    def validate(self, instance, value):
        if len(value.strip()) == 0:
            raise ValueError('value can not be blank')
        return value


class Quantity(Validate):
    def validate(self, instance, value):
        if value < 0:
            raise ValueError('value must be > 0')
        return value


class LineItem:
    description = NoBlank()
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def sub_total(self):
        return self.weight * self.price


if __name__ == '__main__':
    item = LineItem('apple', 15, 20.0)
    print(item.sub_total())