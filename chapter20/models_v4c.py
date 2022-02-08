# -*- coding: utf-8 -*-
# @Time    : 2022/1/18 下午3:33
# @Author  : Zhong Lei
# @FileName: models_v4c.py

class Quantity:
    __counter = 0

    def __init__(self):
        name = self.__class__.__name__
        self.storage_name = '_{}#{}'.format(name, self.__counter)
        self.__counter += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError('value must be > 0')
