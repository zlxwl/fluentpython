# -*- coding: utf-8 -*-
# @Time    : 2021/12/31 下午5:01
# @Author  : Zhong Lei
# @FileName: sequence_slice_hash.py


class Myseq:
    def __getitem__(self, item):
        return item


s = Myseq()
print(s[1])
print(s[1:4])

print(s[1:4:2])

print(s[1:4:2, 9])
print(s[1:4:2, 7:9])

print(slice)
print(dir(slice))