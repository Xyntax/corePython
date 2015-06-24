'''
edit by xy


'''

# -*- coding: utf-8 -*-
#
# def displayNumType(num):
#     print num ,'is',
#     #isinstance同时判断多个种类的用法
#     #如果是这四个其中之一
#     if isinstance(num,(int, long, float, complex)):
#         #返回这个type的名字
#         print 'a number of type:', type(num).__name__
#     else:
# #         print 'not a number at all!!'
#
# displayNumType(-69)
# displayNumType(9999999999999999999999999L)
# displayNumType(98.6)
# displayNumType(-5.2+1.9j)
# displayNumType('xxx')
#

def displayNumType(num):
    print num, 'is',
    if type(num) == type(0):
        print 'an integer'
    elif type(num) == type(0L):
        print 'a long'
    elif type(num) == type(0.0):
        print 'a float'
    elif type(num) == type(0+0j):
        print 'a complex number'
    else:
        print 'not a number at all!!'


