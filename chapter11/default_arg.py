#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xy'


def taxMe(cost, rate=0.0825):
    return cost + (cost * rate)


print taxMe(100)
print taxMe(100, 0.05)


'''
使用默认参数提高程序健壮性
'''