# -*- coding: utf-8 -*-
# @Time    : 2022/1/17 上午10:27
# @Author  : Zhong Lei
# @FileName: osconfeed.py
import json
JSON = '/home/zhonglei/PycharmProjects/fluentpython/chapter19/data/osconfeed.json'


def load():
    with open(JSON) as fp:
        return json.load(fp)
