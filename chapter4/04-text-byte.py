# -*- coding: utf-8 -*-
# @Time    : 2021/12/23 上午11:48
# @Author  : Zhong Lei
# @FileName: 04-text-byte.py


# === 4.1 字符问题 ===
s = "café"
print(len(s))

b = s.encode("utf-8")
print(b)
print(len(b))

b.decode('utf-8')
print(b)


# === 4.2 字节问题 ===
cafe = bytes("café", encoding="utf-8")
print(cafe)
print(cafe[0])
print(cafe[-1])
print(cafe[:2])

cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[0])
print(cafe_arr[:1])
print(cafe_arr[-1:])

print(bytes.fromhex('314BCEA9'))

from array import array
numbers = array('h', [-2, -1, 0, 1, 2])
numbers_arr = bytes(numbers)
print(numbers_arr)
# === 结构体和内存视图 ===
import struct
fmt = '<3s3sHH'
with open("/home/zhonglei/PycharmProjects/fluentpython/chapter4/minst_gan_002.png", "rb") as fp:
    img = memoryview(fp.read())
head = img[:10]
print(head)
bytes(head)
print(head)
print(struct.unpack(fmt, head))

# === 了解编码问题 ===
# === 4.4.2处理 UnicodeDecodeError ===
octets = b'Montr\xe9al'
print(octets.decode('cp1252'))
print(octets.decode('iso8859_7'))
print(octets.decode('koi8_r'))
# print(octets.decode('utf-8'))
