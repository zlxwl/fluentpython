# -*- coding: utf-8 -*-
# @Time    : 2022/1/6 上午10:19
# @Author  : Zhong Lei
# @FileName: iterator_generator.py
from collections import abc


s = 'ABC'
for char in s:
    print(char)

print(isinstance(s, abc.Iterable))
print(issubclass(str, abc.Iterable))


s = 'ABC'
it = iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break


class ArithmeticProcession:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.begin+self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index


def arithmetic_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    index = 0
    forever = end is None
    while forever or result < end:
        yield result
        index += 1
        result = begin + index * step


def arithmetic_pro(begin, step, end=None):
    import itertools
    first = type(begin+step)(begin)
    ap_gen = itertools.count(first, step)
    if end is not None:
        ap_gen = itertools.takewhile(lambda a: a < end, ap_gen)
    return ap_gen


# === 14.10 yield from 关键字　===
# def chain(*iterable):
#     for it in iterable:
#         for i in it:
#             yield i


def chain(*iterable):
    for it in iterable:
        yield from it


if __name__ == '__main__':
    ad = ArithmeticProcession(0, 1, 3)
    print(list(ad))

    ap = ArithmeticProcession(0, 1/3, 1)
    print(list(ap))

    from fractions import Fraction
    ap = ArithmeticProcession(Fraction(0, 1), Fraction(1, 3), Fraction(2, 3))
    print(list(ap))

    from decimal import Decimal
    ap = arithmetic_pro(0, .3, 3)
    print(list(ap))


    s = 'ABC'
    t = tuple(range(3))
    print(list(chain(s, t)))