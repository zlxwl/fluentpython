# -*- coding: utf-8 -*-
# @Time    : 2022/1/19 下午5:53
# @Author  : Zhong Lei
# @FileName: method_is_descriptior.py


import collections


class Text(collections.UserString):
    def __repr__(self):
        return 'Text(!r)'.format(self.data)

    def reverse(self):
        return self[::-1]


if __name__ == '__main__':
    word = Text('forward')
    print(word.reverse().__repr__())

