#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xy'

'''复制文件。提示输入两个文件名（或者使用命令行参数），把第一个文件的内容复制到第二个文件中去。'''

f1 = open(raw_input('enter file path 1: '))
f2 = open(raw_input('enter file path 2: '), 'w')
for i in f1:
    f2.write(i)


'''
rU 或 Ua 以读方式打开, 同时提供通用换行符支持 (PEP 278)
w     以写方式打开，
a     以追加模式打开 (从 EOF 开始, 必要时创建新文件)
r+     以读写模式打开
w+     以读写模式打开 (参见 w )
a+     以读写模式打开 (参见 a )
rb     以二进制读模式打开
wb     以二进制写模式打开 (参见 w )
ab     以二进制追加模式打开 (参见 a )
rb+    以二进制读写模式打开 (参见 r+ )
wb+    以二进制读写模式打开 (参见 w+ )
ab+    以二进制读写模式打开 (参见 a+ )
'''