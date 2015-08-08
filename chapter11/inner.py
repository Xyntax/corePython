#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xy'


def foo():
    def bar():
        print 'bar() called'
    print 'foo() called'
    bar()


foo()
bar()  # 内嵌函数不能在外部调用
