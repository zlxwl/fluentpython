# -*- coding: utf-8 -*-
# @Time    : 2022/1/6 上午11:23
# @Author  : Zhong Lei
# @FileName: sentence_v2.py
import re
import reprlib
from collections import abc
RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence (%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

    def __iter__(self):
        return self


if __name__ == '__main__':
    print(issubclass(SentenceIterator, abc.Iterator))