# -*- coding: utf-8 -*-
# @Time    : 2022/1/4 下午2:09
# @Author  : Zhong Lei
# @FileName: tombola.py
import abc
import random
from collections.abc import Sized


class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self):
        """
        从可迭代对象中添加元素
        """

    @abc.abstractmethod
    def pick(self):
        """随机删除元素，然后将其返回，如果实例为空，这个方法应该抛出‘LookupError’"""

    def loaded(self):
        """如果有至少一个元素返回True, 否则返回False"""
        return bool(self.inspect())

    def inspect(self):
        """返回一个有序元组由当前元素构成"""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))


class Fake(Tombola):
    def pick(self):
        return 12


class BingCage(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except:
            raise LookupError('pick up from empty BingoCage')

    def __call__(self):
        self.pick()


class LotteryBlower(Tombola):
    def __init__(self, iterable):
        self._balls = list(iterable)

    def load(self, iterable):
        return self._balls.extend(iterable)

    def pick(self):
        try:
            postion = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick up from empty LotteryBlower')
        return self._balls.pop(postion)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(sorted(self._balls))


@Tombola.register
class TomboList(list):
    def pick(self):
        if self:
            postion = random.randrange(len(self))
            return self.pop(postion)
        else:
            raise LookupError('pick up from empty LotteryBlower')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))


class AddableBingoCages(BingCage):
    def __add__(self, other):
        if isinstance(other, Tombola):
            return AddableBingoCages(other.inspect() + self.inspect())
        else:
            raise NotImplemented

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        if isinstance(other, Tombola):
            other_iterable = other.inspect()
        else:
            try:
                other_iterable = iter(other)
            except TypeError:
                self_cls = type(self).__name__
                msg = 'right operand in += must be {!r} or an iterable'
                raise TypeError(msg.format(self_cls))
        self.load(other_iterable)
        return self


if __name__ == '__main__':
    # f = Fake()
    print(issubclass(TomboList, Tombola))
    t = TomboList(range(100))
    print(isinstance(t, Tombola))
    print(TomboList.__mro__)
    print(Tombola.__subclasses__())
    balls = list(range(3))
    t = BingCage(balls)
    t.pick()
    print(t.inspect())
    t.pick()
    print(t.inspect())
    t.pick()
    print(t.inspect())

    vowels = 'AEIOU'
    globe = AddableBingoCages(vowels)
    print(globe.inspect())
    print(globe.pick() in vowels)
    print(len(globe.inspect()))

    globe2 = AddableBingoCages('XYZ')
    globe3 = globe + globe2
    print(globe3.inspect())

    # void = globe + [10, 20]
    # print(void)

    globe_org = globe
    globe += globe2
    print(globe.inspect())

    globe += ['M', "N"]
    print(globe2.inspect())
