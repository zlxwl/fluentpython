# -*- coding: utf-8 -*-
# @Time    : 2022/1/5 下午4:23
# @Author  : Zhong Lei
# @FileName: reload_operator.py
import decimal
from collections import Counter


ctx = decimal.getcontext()
print(ctx)
ctx.prec = 40

one_third = decimal.Decimal('1')/decimal.Decimal('3')
print(one_third)
print(one_third == +one_third)


ctx.prec = 20
print(+one_third)
print(one_third == +one_third)

ct = Counter('abracadabra')
print(ct)
ct['r'] = -3
ct['d'] = 0
print(ct)
print(+ct)
