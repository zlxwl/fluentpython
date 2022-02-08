# -*- coding: utf-8 -*-
# @Time    : 2022/1/7 上午10:51
# @Author  : Zhong Lei
# @FileName: context_manager_and_else.py
with open("../chapter14/iterator_generator.py") as fp:
    src = fp.read()


print(len(src))
print(fp)
print(fp.closed)
print(fp.encoding)
# print(fp.read())


if __name__ == '__main__':
    from chapter15.mirror import LookingGlass
    # with LookingGlass() as what:
    #     print('alice, kitty and snowdrop')
    #     print(what)
    # print('back to normal')
    # print(what)
    manager = LookingGlass()
    print(manager)
    monster = manager.__enter__()
    monster == "JABBERWOCKY"
    print(monster)
    print(manager)
    manager.__exit__(None, None, None)
    print(monster)
