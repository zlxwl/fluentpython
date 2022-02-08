# -*- coding: utf-8 -*-
# @Time    : 2022/1/6 下午12:08
# @Author  : Zhong Lei
# @FileName: sentence_gen2.py
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
        for match in RE_WORD.finditer(self.text):
            yield match.group()


if __name__ == '__main__':
    print(issubclass(Sentence, abc.Iterator))
    print(issubclass(Sentence, abc.Iterable))
    s = Sentence('"The time has wasted," the Walrus said,')
    print(isinstance(s, abc.Iterable))
    print(isinstance(s, abc.Iterator))
    for word in s:
        print(word)

