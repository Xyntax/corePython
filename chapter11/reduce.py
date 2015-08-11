#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xy'

def reduce_(bin_func, seq, init=None):
    Iseq = list(seq)
    if init is None:
        res = Iseq.pop()
    else:
        res = init
    for item in Iseq:
        res = bin_func(res, item)
    return res


print 'the total is :', reduce((lambda x, y: x+y), range(5))
