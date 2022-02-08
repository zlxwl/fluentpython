# -*- coding: utf-8 -*-
# @Time    : 2021/12/28 上午10:04
# @Author  : Zhong Lei
# @FileName: 07-decorate.py

# === 7.1装饰器基础知识===
def deco(func):
    def inner():
        print("running inner")
    return inner


@deco
def func():
    print("running func")
func()
print(func)


# === 7.2 python何时执行装饰器 ===
import registration


# === 7.3 使用装饰器改进策略模式 ===
promos = []


def promotion(func):
    promos.append(func)
    return func

# === 7.4 变量作用规则 === python 不要求声明变量，但是在函数体中赋值的是局部变量。
b = 1
def f1(a):
    print(a)
    print(b)


b = 6
def f2(a):
    global b
    print(a)
    print(b)
    b = 9

f2(3)
print(b)
f2(3)

from dis import dis
dis(f1)
dis(f2)

# === 7.5 闭包 ===
class Average():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        return sum(self.series) / len(self.series)

avg = Average()
print(avg(10))
print(avg(11))
print(avg(12))


def make_average():
    series = []
    def average(new_value):
        series.append(new_value)
        return sum(series)/len(series)
    return average

avg = make_average()

print(avg(10))
print(avg(11))
print(avg(12))

print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)
print(avg.__closure__)
print(avg.__closure__[0].cell_contents)


# === 7.6 nonlocal 声明 ===
def make_average():
    count = 0
    total = 0

    def average(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total/count

    return average

avg = make_average()
print(avg(10))
print(avg(11))
print(avg(12))


# === 7.7 实现一个简单的装饰器 ===
import time


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        args_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, args_str, result))
        return result
    return clocked

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n <2 else n*factorial(n-1)


if __name__ == '__main__':
    print('*'*40, 'Calling snooze(.123)')
    snooze(.123)
    print('*'*40, 'Calling factorial(6)')
    print('!6 =', factorial(6))