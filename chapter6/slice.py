# -*- coding: utf-8 -*-
__author__ = 'xy'

#切片（slice）的扩展使用方法

#1 用步长索引来进行扩展的切片操作
# slice[1:2:3]其中第3个位置表示步长，默认为1

#简单的str翻转:
s = 'abcde'
print s[::-1]
# >>>'edcba'

#间隔一个字符取值：
print s[::2]
# >>>'ace'

#2 切片索引不越界
print ('a', 'b', 'c')[-100:100]
# >>>('a','b','c')

#3 [None]对for循环的增强：
#每次循环把最后一个字符干掉：
s = 'abcde'
i = -1
for i in range(-1, len(s), -1):
    print s[:i]
# >>>
# abcd
# abc
# ab
# a
#如果想要第一次的时候完整输出'abcde'，一般需要在for前增加一条print语句
#看下面改进：
s = 'abcde'
for i in [None]+range(-1, -len(s), -1):
    print s[:i]
# >>>
# abcde
# abcd
# abc
# ab
# a