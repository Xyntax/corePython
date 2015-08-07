#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xy'

'''
Python文档字符串。进入Python标准库所在的目录，检查每个.py文件看是否有__doc__字符串，
如果有，对其格式进行适当的整理归类。你的程序执行完毕后，应该会生成一个漂亮的清单，
里边列出哪些模块有文档字符串，以及文档字符串的内容，清单最后附上那些没有文档字符串模块的名字。
'''

import os
import sys

# for linux

num = []
# iterate
def fun(dirname):
    for i in os.listdir(dirname):
        if os.path.isdir(dirname + '/' + i):
            fun(dirname + '/' + i)
        else:
            num.append(dirname + '/' + i)

path = r'/usr/lib/python2.7'
fun(path)
hasDoc = False
strTemp = ''
fobj1 = open('hasdoc.txt', 'a+')
fobj2 = open('nodoc.txt', 'a+')

for i in num:
    fobj = open(i)
    for eachline in fobj:
        if (not hasDoc) and eachline.startswith('"""'):
            hasDoc = True
        elif hasDoc and eachline.startswith('"""'):
            hasDoc = False
            strTemp += eachline
            break
        if hasDoc:
            strTemp += eachline
        else:
            break
    if strTemp != '':
        fobj1.write('filename: ' + i + '\n')
        fobj1.write('_doc_ is: \n' + strTemp + '\n')
    else:
        fobj2.write('filename: ' + i + '\n')
    strTemp = ''
    fobj.close()

fobj1.close()
fobj2.close()

'''
注意递归遍历文件的方式
提取doc的内容待优化
'''