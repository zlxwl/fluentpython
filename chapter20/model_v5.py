# -*- coding: utf-8 -*-
# @Time    : 2022/1/18 下午6:47
# @Author  : Zhong Lei
# @FileName: model_v5.py
import abc


class AutoStorage:
    __counter = 0

    def __init__(self):
        prefix = self.__class__.__name__
        index = self.__counter
        self.storage_name = '_{}#{}'.format(prefix, index)
        self.__counter += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)


class Validated(abc.ABC, AutoStorage):

    def __set__(self, instance, value):
        value = self.validate(instance, value)
        super().__set__(instance, value)

    @abc.abstractmethod
    def validate(self):
        pass


class Quantity(Validated):
    def validate(self, instance, value):
        if value > 0:
            return value
        else:
            raise ValueError('value must be > 0')


class NonBlank(Validated):
    def validate(self, instance, value):
        value = value.strip()
        if len(value) == 0:
            raise ValueError('value cannot be blank')
        return value


def entity(cls):
    for key, value in cls.__dict__.items():
        if isinstance(value, Validated):
            name = type(value).__name__
            value.storage_name = '_{}#{}'.format(name, key)
    return cls


class EntityMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        for key, value in attrs.items():
            if isinstance(value, Validated):
                type_name = type(value).__name__
                value.storage_name = '_{}#{}'.format(type_name, key)


class Entity(metaclass=EntityMeta):
    pass