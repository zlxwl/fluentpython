# -*- coding: utf-8 -*-
# @Time    : 2022/1/17 下午4:19
# @Author  : Zhong Lei
# @FileName: blackknight.py


class BlackKnight:
    def __init__(self):
        self.members = ['an arm', 'another arm', 'a leg', 'another leg']
        self.phrases = ['Tis but a scrach', 'it is just a flesh wound', 'i am invinciable']

    @property
    def member(self):
        print('next members is:')
        return self.members[0]

    @member.deleter
    def member(self):
        text = 'BLACK KNIGHT (lossed {}\n -- {})'
        print(text.format(self.members.pop(0), self.phrases.pop(0)))


if __name__ == '__main__':
    knight = BlackKnight()
    print(knight.member)
    del knight.member
    del knight.member
    del knight.member
    del knight.member