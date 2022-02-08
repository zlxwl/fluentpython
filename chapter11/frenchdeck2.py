# -*- coding: utf-8 -*-
# @Time    : 2022/1/4 上午11:42
# @Author  : Zhong Lei
# @FileName: frenchdeck2.py
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


# === 11.5 定义抽象基类的子类 ===
class FrenchDeck2(collections.MutableSequence):
    ranks = [x for x in range(2, 11)] + list('JKQA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
       self._cards = [Card(rank=rank, suit=suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):
        self._cards[key] = value

    def __delitem__(self, key):
        del self._cards[key]

    def insert(self, position, value):
        self._cards.insert(position, value)


if __name__ == '__main__':
    frenchcards = FrenchDeck2()
