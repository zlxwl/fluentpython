# -*- coding: utf-8 -*-
# @Time    : 2021/12/28 下午7:10
# @Author  : Zhong Lei
# @FileName: prameter_clock.py
import time

DEFAULT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

# 参数化装饰器比普通装饰器外面多了一层用于传递参数，中间层是装饰器，最内层是参数器执行的功能。
# python支持闭包和自由变量绑定， decorate内能访问clock中传递的变量fmt; 同理clocked能访问decorate中的func和clock中的fmt.所以闭包和自由变量绑定支持了python装饰器语法
# 函数的调用 clock(fmt)(func)(args) 　1.调用clock(fmt) -> 返回decorate函数　2. 调用decorate(func)　-> 返回clocked函数 3. 调用clocked(args)　-> 实际执行装饰器功能和函数功能。
# 从外层向内层调用，　python中的函数是一等对象，所以函数可以作为参数返回，也可以作为结果返回。　func没有括号的便是函数的引用。这个是实现装饰器的第二个关键要素。
# 其他特性，装饰器函数在导入时就运行了。闭包中的不可变局部变量（str, int, tuple, set），如果有就地赋值和改变，会被判定为局部变量，如果要访问并改变需要添加nonlocal关键字。


def clock(fmt=DEFAULT):
    def decorate(func):
        def clocked(*_args):
            t0 = time.perf_counter()
            _result = func(*_args)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))
            return _result
        return clocked
    return decorate


if __name__ == '__main__':
    # @clock()
    # def snooze(seconds):
    #     time.sleep(seconds)

    # @clock('{name}: {elapsed}s')
    # def snooze(seconds):
    #     time.sleep(seconds)
    # @clock('{name} ({args}) dt={elapsed}s / result')
    def snooze(seconds):
        time.sleep(seconds)
        return 'success!'


    # for i in range(3):
    #     snooze(.123)
    for i in range(3):
        clock('{name} ({args}) dt={elapsed}s / result')(snooze)(.123)
