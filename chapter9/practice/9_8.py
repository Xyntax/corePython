#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xy'

'''
模块研究：提取模块的属性资料。
提示用户输入一个模块名（或者从命令行接受输入）。然后使用dir()和其他内建函数提供模块的属性，显示他们的名字、类型、值
'''

name = raw_input('module name: ')
obj = __import__(name)
ls = dir(obj)
for item in ls:
    print 'name: ', item
    print 'type: ', type(getattr(obj, item))
    print 'value: ', getattr(obj, item)
    print ''
