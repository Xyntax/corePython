#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xy'


def map_(func, seq):
    mapped_seq = []
    for eachItem in seq:
        mapped_seq.append(func(eachItem))
    return mapped_seq


print map(lambda x: x**2, range(6))
print map(lambda x, y: x+y, [1, 2], [3, 4])  # 用两个list输入两个参数
print map(None, [1, 3, 5], [2, 4, 6])  # 功能与zip()相同
