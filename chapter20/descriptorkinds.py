# -*- coding: utf-8 -*-
# @Time    : 2022/1/18 下午8:43
# @Author  : Zhong Lei
# @FileName: descriptorkinds.py


def cls_name(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]


def display(obj):
    cls = type(obj)
    if cls is type:
        return '<class {}>'.format(obj.__name__)
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return '<{} object>'.format(cls_name(obj))


def print_args(name, *args):
    pseudo_args = ', '.join(display(x) for x in args)
    print('-> {}.__{}__({})'.format(cls_name(args[0]), name, pseudo_args))


class Overriding:
    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class OverridingNoGet:
    def __set__(self, instance, value):
        print_args('set', self, instance, value)


class NonOveriding:
    def __get__(self, instance, owner):
        print('get', self, instance, owner)


class Managed:
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NonOveriding()

    def spam(self, x, y):
        print('spam')
        print('-> managed.spam({})'.format(display(self)))
        print(x + y)


if __name__ == '__main__':
    obj = Managed()
    # obj.over
    # Managed.over
    # obj.over = 7
    # obj.over
    #
    # obj.__dict__['over'] = 8
    # print(vars(obj))
    # obj.over
    # print(vars(obj))

    # 20-10
    # obj.over_no_get
    # Managed.over_no_get
    # obj.over_no_get = 7
    # obj.over_no_get
    # obj.__dict__['over_no_get'] = 9
    # print(obj.over_no_get)
    # obj.over_no_get = 7
    # print(obj.over_no_get)

    # 20-11
    obj = Managed()
    obj.non_over
    obj.non_over = 7
    print(obj.non_over)
    Managed.non_over
    del obj.non_over
    obj.non_over

    # 20-12
    # obj = Managed()
    # Managed.over = 1
    # Managed.over_no_get = 2
    # Managed.non_over = 3
    # print(obj.over, obj.over_no_get, obj.non_over)

    # 20-13
    # obj = Managed()
    # print(obj.spam)
    # print(Managed.spam)
    # obj.spam = 7
    # print(obj.spam)

    # # bound_method, obj.spam
    # bound_method = Managed.spam.__get__(obj)
    # print(bound_method.__func__.__call__(bound_method.__self__, 3, 4))
    # print(obj.spam(3, 4))


