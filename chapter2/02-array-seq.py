# -*- coding: utf-8 -*-
# @Time    : 2021/12/20 下午5:07
# @Author  : Zhong Lei
# @FileName: 02-array-seq.py

# ===== 1 =====
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)


# === 2.2.2 filter & map===
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)


# === 2.2.3 笛卡尔积 ===
colors = ["black", "white"]
sizes = ["L", "M", "S"]
tshirt = [(color, size) for color in colors for size in sizes]
print(tshirt)
tshirt = [(color, size) for size in sizes for color in colors]
print(tshirt)


# === 2.2.4 生成器表达式 ===
print(tuple(ord(s) for s in symbols))
import array
print(array.array("I", (ord(s) for s in symbols)))
for tshirt in ("%s %s" %(c, s) for c in colors for s in sizes):
    print(tshirt)


# === 2.3.1 元组与记录 ===
lax_coordinates = (33.924, -118.408056)
city, year, pop, chg, area = ("Tokyo", 2003, 324450, 0.66, 8014)
travel_ids = [("USA", "31195855"), ("BRA", "CE342567"), ("ESP", "XDA208556")]
for passport in sorted(travel_ids):
    print("%s/%s" % passport)
for country, _ in travel_ids:
    print(country)


# === 2.3.2 元组拆包 ===
a = divmod(20, 8)
print(a)
print(divmod(*a))

import os
_, filename = os.path.split("aa/a.txt")
print(filename)

# 通过*来获取不确定的参数
a, b, *rest = range(5)
print(rest)


# === 2.3.3 嵌套元组拆包 ===
metro_ares = [
    ("tokyo", "jp", 36.933, (35.689722, 139.691667)),
    ("delhi ncr", "in", 21.935, (28.613889, 77.208889)),
    ("mexico city", "mx", 20.142, (19.433333, -99.133333)),
    ("new york", "us", 20.104, (40.808611, -74.020386)),
    ("sao pualo", "br", 19.649, (-23.547778, -46.635833))
]
print("{:15} | {:^9} | {:^9}".format(" ", "lat.", "long."))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, c, pop, (lat, long) in metro_ares:
    if long <= 0:
        print(fmt.format(name, lat, long))


# === 2.3.4 具名元组 ===
from collections import namedtuple
City = namedtuple("City", ["name", "country", "population", "coordinates"])
tokyo = City("tokyo", "jp", 36.933, (35.689722, 139.691667))
print(tokyo)
print(tokyo._fields)
print(tokyo._asdict())

LatLong = namedtuple("LatLone", ["Lat", "Long"])
delhi = ("delhi ncr", "in", 21.935, LatLong(26.613889, 77.208889))
delhi = City._make(delhi)
print(delhi)


# === 2.5 对序列使用+, * ===
board = [['_'] * 3 for i in range(3)]
board[1][2] = 'X'
print(board)

board = [['_'] * 3] * 3#指向同一个列表并复制三次
board[1][2] = "X"
print(board)


# === 2.6 序列的增量赋值 ===
l = [1, 2, 3]
print(id(l))
l *= 2
print(id(l))

t = (1, 2, 3)
print(id(t))
t *= 2
print(id(t))

# t = (1, 2, [1, 2])
# t[2] += [20, 30]
# print(t)


# === 2.7 list.sort方法和内置函数sorted方法 ===
fruits = ['grape', 'raspberry', 'apple', 'banana']
sorted(fruits)
print(fruits)
print(sorted(fruits, key=len))
print(sorted(fruits, reverse=True, key=len))
print(fruits)
fruits.sort()
print(fruits)


# === 2.8 用bisect来管理已排序的序列 ===
# === 2.8.1用bisect来搜索 ===
import bisect
HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = "{0:2d} @ {1:2d}     {2}{0:<2d}"


def demo(bisect_fn: bisect.bisect):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)
        offset = position * "|"
        print(ROW_FMT.format(needle, position, offset))


if __name__ == '__main__':
    bisect_fn = bisect.bisect
    print("Demo:", bisect_fn.__name__)
    print("haystack ->", " ".join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)


# 根据一个分数找到他所对应的成绩
def grade(score, breakpoints=[60, 70, 80, 90], grades="FDCBA"):
    index = bisect.bisect(breakpoints, score)
    return grades[index]
print([grade(score) for score in [33, 99, 77, 89, 90, 100]])


# === 2.8.2 用bisect.insort插入新元素 ===
import random
import bisect

SIZE = 7
random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(2*SIZE)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)


# === 当列表不是首选时2.9 ===
# === 2.9.1 数组===
from array import array
from random import random
floats = array('d', (random() for i in range(10**7)))
print(floats[-1])
with open("floats.bin", 'wb') as f:
    floats.tofile(f)

floats2 = array('d')
with open("floats.bin", 'rb') as f:
    floats2.fromfile(f, 10**7)
print(floats2[-1])
print(floats2 == floats)
# === 2.9.2 内存视图===
numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
print(memv[2])
memv_obt = memv.cast('B')
memv_obt.tolist()
memv_obt[5] = 4
print(numbers)
# === 2.9.3 Numpy and Scipy ===
import numpy as np
a = np.arange(12)
print(a)
a.shape = 3, 4
print(a)
print(a[2, :])
print(a[2, 1])
print(a.transpose())
np.save("floats.npy", a)
floats = np.load("floats.npy")
print(floats)
# === 2.9.4 双向队列 ===
from collections import deque
dq = deque(range(10), maxlen=10)
print(dq)
dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)
dq.appendleft(-1)
print(dq)
dq.extend([11, 22, 33])
print(dq)
dq.extendleft([10, 20, 30, 40])
print(dq)

# === use namedtuple instead dict ===
import json
from collections import namedtuple
with open("/home/zhonglei/PycharmProjects/fluentpython/chapter3/8-1-new.json", "r", encoding="utf-8") as f:
    datas = dict(json.loads(f.read())).get("rasa_nlu_data").get("common_examples")


example = namedtuple("example", ['text', 'intent', 'entities'])
examples = (example(data["text"], data['intent'], data['entities']) for data in datas)
for item in examples:
    print(item[0])