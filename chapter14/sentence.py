# -*- coding: utf-8 -*-
# @Time    : 2022/1/6 上午10:33
# @Author  : Zhong Lei
# @FileName: sentence.py
import re
import reprlib
from collections import abc

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(self.text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


if __name__ == '__main__':
    s = Sentence('"The time has wasted," the Walrus said,')
    for word in s:
        print(word)

    print(issubclass(Sentence, abc.Iterable))
    print(isinstance(s, abc.Iterable))

    it = iter(s)
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))