# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 下午4:31
# @Author  : Zhong Lei
# @FileName: model_v6.py
import abc
from collections import OrderedDict


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


class MetaEntity(type):
    @classmethod
    def __prepare__(metacls, name, bases):
        return OrderedDict()

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls._fields = []
        for key, value in attrs.items():
            if isinstance(value, Validated):
                type_name = type(value).__name__
                storage_name = '_{}#{}'.format(type_name, key)
                setattr(cls, storage_name, value)
                cls._fields.append(key)


class Entity(metaclass=MetaEntity):
    @classmethod
    def field_names(cls):
        for name in cls._fields:
            yield name