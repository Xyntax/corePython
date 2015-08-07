#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xy'

path = raw_input('enter file path')
read_line = raw_input('enter line num')  # raw_input()是string 要用int转一下
fobj = open(path, 'r')
for i in range(int(read_line)):
    print fobj.readline()
fobj.close()  # 好习惯！


# ans:遍历方式（直接用in就可以按行遍历）
# for eachline in fobj:
#     print eachline

