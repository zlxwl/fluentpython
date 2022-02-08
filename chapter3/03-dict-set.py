# -*- coding: utf-8 -*-
# @Time    : 2021/12/22 上午10:44
# @Author  : Zhong Lei
# @FileName: 03-dict-set.py


# === 3.2 字典推导 ===
dial_coded = [(86, 'China'), (91, 'India'), (1, 'United States'), (62, 'Indonesia'), (55, 'Brazil'),
              (92, 'Pakistan'), (880, 'Bangladesh'), (234, 'Nigeria'), (7, 'Russia'), (81, 'Japan')]
country_code = {country: code for code, country in dial_coded}
print(country_code)
code_country = {code: country.upper() for code, country in dial_coded if code < 66}
print(code_country)

# === 3.3常见的映射方法 ===
from collections import defaultdict

index_dict = defaultdict(list)
index_dict["dd"].append("a")
print(index_dict)

index_dict = {}
index_dict.setdefault("aa", []).append("c")
print(index_dict)
# 在插入不存在的值的两种方法，减少了查询的次数。后台是通过__miss__()方法实现，get()方法返回结果是none __getitem__()


# === 3.4.2 __missing__特殊方法 ===
class StrKeyDict0(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, item):
        return item in self.keys() or str(item) in self.keys()

d = StrKeyDict0([('2', 'two'), ('4', 'four')])
print(d['2'])
print(d['4'])
print(d.get(1, 'n/a'))

# === 3.5 字典的变种 ===
from collections import ChainMap
pylookup = ChainMap(locals(), globals(), vars())
print(pylookup)

from collections import Counter
ct = Counter('abracadabra')
print(ct)
ct.update("aaaaazzz")
print(ct)
print(ct.most_common(3))

# === 3.6 UserDict === 对于用户自定义的词典来，不要继承dict而是直接继承userdict, userdict的data属性是dict的实例
from collections import UserDict
class StrKeyDict(UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.keys()

    def __setitem__(self, key, value):
        self.data[str(key)] = value


# === 3.7 不可变映射类型 ===
from types import MappingProxyType
d = {1: 'A'}
map = MappingProxyType(d)
print(map)
d[2] = 'b'
print(map)

# === 3.8 集合 ===
# === 3.8.2 集合推导 ===
from unicodedata import name
print({chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')})

# === 3.9 dict和set背后 ===
# === 3.9.1 一个关于效率的实验 ===
