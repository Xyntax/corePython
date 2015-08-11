#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xy'

def filter_(bool_func, seq):
    filtered_seq = []
    for eachItem in seq:
        if bool_func(eachItem):
            filtered_seq.append(eachItem)
    return filtered_seq


from random import randint


def odd(n):
    return n % 2


allNums = []
for eachNum in range(9):
    allNums.append(randint(1, 99))

print filter(odd, allNums)

# 第一次改进： print filter(lambda x: x % 2, allNums)
# 第二次改进：用list-if代替filter  print [n for n in allNums if n%2]
# 第三次改进： print [n for n in [randint(1, 99) for i in range(9)] if n%2]
