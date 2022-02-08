# -*- coding: utf-8 -*-
# @Time    : 2022/1/4 下午6:04
# @Author  : Zhong Lei
# @FileName: multi_extends.py


# === 12.2多重继承和方法解析顺序 ===
class A:
    def ping(self):
        print('ping', self)


class B(A):
    def pong(self):
        print('pong', self)


class C(A):
    def pong(self):
        print('PONG', self)


class D(B, C):
    def ping(self):
        super(D, self).ping()
        print('post-ping', self)

    def pingpong(self):
        self.ping()
        super(D, self).ping()
        self.pong()
        super(D, self).pong()
        C.pong(self)


def print_cls(cls):
    print(','.join(c.__name__ for c in cls.__mro__))


if __name__ == '__main__':
    d = D()
    d.pong()
    C.pong(d)
    d.pingpong()
    print(D.__mro__)
    d.ping()

    import io, numbers, tkinter
    print_cls(bool)
    print_cls(numbers.Integral)
    print_cls(io.BytesIO)
    print_cls(io.TextIOWrapper)
    print_cls(tkinter.Text)
    print(len(dir(tkinter.Button)))