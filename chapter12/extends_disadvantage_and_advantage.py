# -*- coding: utf-8 -*-
# @Time    : 2022/1/4 下午5:54
# @Author  : Zhong Lei
# @FileName: extends_disadvantage_and_advantage.py
from collections import UserDict


class DoppedDict(dict):
    def __setitem__(self, key, value):
        super(DoppedDict, self).__setitem__(key, [value]*2)


class AnswerDict(dict):
    def __getitem__(self, item):
        return 42


class DoppedUserDict(UserDict):
    def __setitem__(self, key, value):
        super(DoppedUserDict, self).__setitem__(key, [value]*2)


class AnswerUserDict(UserDict):
    def __getitem__(self, item):
        return 42


if __name__ == '__main__':
    dd = DoppedUserDict(one=1)
    print(dd)
    dd['two'] = 2
    print(dd)
    dd.update(three=3)
    print(dd)

    aa = AnswerUserDict(one=1)
    print(aa)
    print(aa.get("one"))
    print(aa["one"])
    d = {}
    d.update(aa)
    print(d['one'])