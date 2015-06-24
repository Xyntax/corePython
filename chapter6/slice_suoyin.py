# -*- coding: utf-8 -*-
__author__ = 'xy'

s = 'abcde'
s1 = s[0:5]
print s1
#abcde(0,1,2,3,4)

s2 = s[-5:-3]
print s2
#ab(-5,-4)

s3 = s[-5:0]
print s3
#不反回任何值
#s[-5]本身就是s[0]

s4 = s[-5:-1]
print s4
#abcd(-5,-4,-3,-2)

s5 = s[-5:]
print s5
#abcde

#无论正序倒序都是一样，访问头不访问尾，倒序不能输出完整序列，只能这样s[-5:]
