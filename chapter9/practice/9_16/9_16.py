#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xy'

'''
文本处理。
人们输入的字符常常超过屏幕的最大宽度，编写一个程序，在一个文本文件中查找长度大于80个字符的文本行。
#从最接80个字符的单词断行，把剩余的文件插入到下一行处。程序执行完毕后，应该没有超过80个字符的文本行了。
'''

path = raw_input('enter file path:')
# file1 = open(path, 'r')
file1 = open('./test80.txt')
tmp_file = open('./tmp.txt', 'w+')

lines = file1.readlines()
file1.close()

nextstr = ''
new_line = ''
for n in range(len(lines)):
    if nextstr != '':
        new_line = nextstr + lines[n]
    else:
        new_line = lines[n]
    str1 = ''
    nextstr = ''
    if len(lines[n]) > 80:
        char80 = new_line[0:80]
        for i, ch in enumerate(char80[::-1]):
            print i, ch
            if ch in ' ,.':
                str1 = char80[:80 - i]
                nextstr = new_line[80 - i:]
                break
            else:
                str1 = new_line[:80]
        tmp_file.write(str1)
    else:
        tmp_file.write(lines[n])
tmp_file.close()

