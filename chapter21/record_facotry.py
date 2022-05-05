# -*- coding: utf-8 -*-
# @Time    : 2022/5/5 上午10:23
# @Author  : Zhong Lei
# @FileName: record_facotry.py
import types


def record_factory(cls_name, field_names):
    try:
        field_names = field_names.split(',', ' ').split()
    except AttributeError:
        pass

    field_names = tuple(field_names)

    def __init__(self, *args, **kwargs):
        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)
        for name, value in attrs.items():
            setattr(self, name, value)

    def __iter__(self):
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self):
        values = ', '.join('{}={!r}'.format(*i) for i in zip(self.__slots__, self))
        return '{}({})'.format(self.__class__.__name__, values)

    cls_attr = dict(__slots__=field_names,
                    __init__=__init__,
                    __iter__=__iter__,
                    __repr__=__repr__)
    return type(cls_name, (object, ), cls_attr)
    # return types.new_class(cls_name, (object, ), cls_attr)


if __name__ == '__main__':
    Dog = record_factory('Dog', ['name', 'weight', 'owner'])
    dog = Dog('apple', 40, 'marry')
    print(dog)