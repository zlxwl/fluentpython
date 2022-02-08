# -*- coding: utf-8 -*-
# @Time    : 2021/12/28 下午4:16
# @Author  : Zhong Lei
# @FileName: singledispatch.py
import html
from collections import abc
from functools import singledispatch
import numbers


@singledispatch
def htmlized(obj):
    content = html.escape((repr(obj)))
    return '<pre>{}</pre>'.format(content)


@htmlized.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)


@htmlized.register(numbers.Integral)
def _(n):
    return '<pre>{0}(0x{0:x})</pre>'.format(n)


@htmlized.register(tuple)
@htmlized.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlized(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


print(htmlized({1, 2, 3}))
print(htmlized(abs))


print(htmlized('a'))
print(htmlized(42))
print(htmlized(['alpha', 66, {1, 2, 3}]))

