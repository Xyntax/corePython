# -*- coding: utf-8 -*-
__author__ = 'xy'

# 字符串操作符与格式控制

'''
----------------------------
%c  ASC2或者长度为1的字符串

%s  __str__()
%r  __repr__()

%d %i  有符号十进制
%u  无符号十进制

%o  无符号八进制

%x %X  无符号十六进制

%e %E  科学计数法

%f %F  float（小数部分自动截断）

%g %G  ==%e+%f ==%E+%F

%%  print '%'

-----------------------------

*       定义宽度或小数点精度
-       左对齐
+       在正数前面显示加号
<sp>    在正数前面显示空格
#       八进制显示0,十六进制显示0X或者0x
0       数字前面填充0而不是空格
(var)   映射变量，字典参数
m.n     最小总宽度，小数点后的位数

-----------------------------
'''

'''
#test 0x00
print '%x' % 108, '%X' % 108
'6c 6C'

print '%#X' % 108
'0X6C'

#test f e E .2 g G
print '%.2f' % 1.2345678
'1.23'

print '%E' % 1234.567890
'1.234568E+03'

print '%g' % 1234.567890
'1234.57'

#test +d i s o
print '%+d' % 4
'+4'

print '%+d' % -4
'+4'

print '%d%%' % 100
'100%'

print '%s %s' % ('hello', 'world')
'hello world'

print '%#o/hex' % 123
'0173/hex'

print '%02d/%02d/%02d' % (2, 15, 67)
'02/15/67'

#test dict
print 'There are %(key1)d %(key2)s Quotation Symbals' % \
      {'key2': 'Python', 'key1': 3}
'There are 3 Python Quotation Symbals'

'''

'''
一种针对dict更方便的表示方法——使用${}

from string import Template

s = Template('There are ${key1} ${key2} Quotations Symbols')

print s.substitute(key2='Python', key1=3)
'There are 3 Python Quotation Symbals'

print s.substitute(key2='Python')
'KeyError: 'key1''

print s.safe_substitute(key2='Python')
'There are ${key1} Python Quotations Symbols'

'''

'''
#u/U and r/R
ur'Hello\nWorld!'
'''