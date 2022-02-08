# -*- coding: utf-8 -*-
# @Time    : 2021/12/29 上午11:04
# @Author  : Zhong Lei
# @FileName: object_reference_mutable.py

# === 8.1 变量不是盒子 ===
class Gizmo:
    def __init__(self):
        print('gizmo %d' % id(self))

x = Gizmo()

print(dir())


# === 8.2 is和== ===
# is比较的是两个对象的id, 不能被重载；　==调用的是对象实现的__eq__()方法。

# === 8.2.2 元组的相对不可变性 ===
t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])

print(t1 == t2)
print(id(t1[-1]))
t1[-1].append(50)
print(t1)
print(id(t1[-1]))
print(t1 == t2)


# ===8.3 默认做浅复制 ===
l1 = [1, 2, 3]
l2 = l1[:]
print(l1 == l2)
print(l1 is l2)

l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = l1[:]
l1.append(100)
l1[1].remove(55)
print("l1->", l1)
print('l2->', l2)

l1[1] += [33, 22]
l2[2] += (10, 11)
print('l1:', l1)
print('l2:', l2)

# === 为任意对象做浅复制和深复制 ===
class Bus:
    def __init__(self, passengers):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


import copy
bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
print((id(bus1), id(bus2), id(bus3)))
bus1.drop('Bill')
print(bus2.passengers)
print(bus3.passengers)
print((id(bus1.passengers), id(bus2.passengers), id(bus3.passengers)))



# === 8.4函数的参数作为引用时 ===
def f(a, b):
    a += b
    return a

x, y = 1, 2
print(f(x, y))
print(x, y)

a = [1, 2]
b = [3, 4]
print(f(a, b))
print(a)
print(b)

t = (10, 20)
u = (30, 40)
print(f(t, u))
print(t, u)

# === 8.4.1 不要使用可变类型参数的默认值 ===
class HauntedBus:
    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

bus1 = HauntedBus(['Alice', 'Bill'])
print(bus1.passengers)
bus1.pick('Claire')
bus1.drop('Alice')
print(bus1.passengers)

bus2 = HauntedBus()
bus2.pick('Carrie')
print(bus2.passengers)

bus3 = HauntedBus()
print(bus3.passengers)
bus3.pick("David")
print(bus3.passengers)
print(bus2.passengers)

print(bus3.passengers is bus2.passengers)
print(bus1.passengers)

print(HauntedBus.__init__.__defaults__)
print(HauntedBus.__init__.__defaults__[0] is bus2.passengers)


class TwilightBus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            # self.passengers = list(passengers)
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

basketball_team = ['sue', 'tina', 'maya', 'dina', 'pat']
bus = TwilightBus(basketball_team)
bus.drop('sue')
bus.drop('tina')
print(basketball_team)


# === 8.5 del和垃圾回收 ===
import weakref
s1 = {1, 2, 3}
s2 = s1
def bye():
    print('Gone with the wind')

ender = weakref.finalize(s1, bye)
print(ender.alive)

del s1
print(ender.alive)
s2 = 'spam'
print(ender.alive)

# === 8.6 弱引用 ===
print("*"*40 +"weakref")
import weakref
a_set = {1, 2, 3}
wref = weakref.ref(a_set)
print(wref)
print(wref())
a_set = {2, 3, 4}
print(wref())
print(wref() is None)
print(wref() is None)


# === 8.6.1 WeakValueDictionary ===
class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'cheese (%r)' % (self.kind)

stock = weakref.WeakValueDictionary()
catlog = [Cheese('Red L'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Paramsan')]
for cheese in catlog:
    stock[cheese.kind] = cheese
print(sorted(stock.keys()))
del catlog
print(sorted(stock.keys()))
del cheese
print(sorted(stock.keys()))


# === 8.7 python对不可变类型施加的把戏 ===
