# -*- coding: utf-8 -*-
# @Time    : 2022/1/6 上午11:38
# @Author  : Zhong Lei
# @FileName: sentence_gen.py
import re
import reprlib
from collections import abc

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word


if __name__ == '__main__':
    s = Sentence('"The time has wasted," the Walrus said,')
    for word in s:
        print(word)

    print(isinstance(s, abc.Iterator))
    print(isinstance(s, abc.Iterable))