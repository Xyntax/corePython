#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xy'


is_this_global = 'xyz'
def foo():
    global is_this_global  # 在局部使用全局变量之前先声明gloabl
    this_is_global = 'abc'
    is_this_global = 'def'
    print this_is_global + is_this_global

foo()
