# -*- coding: utf-8 -*-
# @Time    : 2021/12/24 下午12:04
# @Author  : Zhong Lei
# @FileName: 05-function.py

# === 5.1 把函数视作对象 ===
def factorial(n):
    '''
    :param n:
    :return: returns n
    '''
    return 1 if n < 2 else n * factorial(n-1)

print(factorial(42))
print(factorial.__doc__)
print(type(factorial))

fact = factorial
print(fact)
print(fact(5))
print(map(fact, range(11)))
print(list(map(fact, range(11))))

# === 5.2 使用高阶函数 === 把函数作为参数传入，把函数作为结果返回
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))


def reverse(word):
    return word[::-1]

print(reverse('testing'))
print(sorted(fruits, key=reverse))

# === 5.3　匿名函数 ===
print(sorted(fruits, key=lambda word: word[::-1]))

# === 5.4 可调用对象 ===
print([callable(obj) for obj in (abs, str, 13)])

# === 5.5 使用用户定义的可调用类型 ===
import random
class Bingo:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("pick up from empty list")

    def __call__(self):
        return self.pick()

bingo = Bingo(range(10))
print(bingo.pick())
print(bingo())
print(callable(bingo))

print(dir(bingo))
print(dir(factorial))

print(sorted(set(dir(factorial))-set(dir(bingo))))

# === 5.6 函数内省 ===
class C: pass
def func():
    pass
c = C()
print(sorted(set(dir(func)) - set(dir(c))))

# === 5.7 从定位参数到仅限关键字参数 ===
def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls

    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''

    if content:
        return "\n".join('<%s%s>%s<%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)

print(tag('br'))
print(tag('p', 'hello'))
print(tag('p', 'hello', 'world'))
print(tag('p', 'hello', id=33))
print(tag('p', 'hello', 'world', cls='sidebar'))
print(tag(content='testing', name='img'))
my_tag = {'name': 'img', 'title': 'student', 'src': 'sunset.jpg', 'cls': 'framed'}
print(tag(**my_tag))

# === 5.8 获取关于参数的信息 ===
