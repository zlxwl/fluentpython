# -*- coding: utf-8 -*-
# @Time    : 2022/1/6 下午1:04
# @Author  : Zhong Lei
# @FileName: sentence_genexp.py
import re
import reprlib
from collections import abc

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))


if __name__ == '__main__':
    s = Sentence('"The time has wasted," the Walrus said,')
    print(isinstance(s, abc.Iterable))
    print(isinstance(s, abc.Iterator))
    for word in s:
        print(word)

