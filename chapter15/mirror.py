# -*- coding: utf-8 -*-
# @Time    : 2022/1/7 上午11:00
# @Author  : Zhong Lei
# @FileName: mirror.py
import sys


class LookingGlass:
    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exec_type, exec_value, traceback):
        sys.stdout.write = self.original_write
        if exec_type is ZeroDivisionError:
            print('please do not divide by zero!')
            return True


