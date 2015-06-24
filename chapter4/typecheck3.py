'''
edit by xy


'''

# -*- coding: utf-8 -*-
#


# def displayNumType(num):
#     print num, 'is',
#     if type(num) == type(0):
#         print 'an integer'
#     elif type(num) == type(0L):
#         print 'a long'
#     elif type(num) == type(0.0):
#         print 'a float'
#     elif type(num) == type(0+0j):
#         print 'a complex number'
#     else:
#         print 'not a number at all!!'
#
#
# #减少函数调用的次数
# #代码在进行判断时使用了两次type()函数，我们使用types模块中的变量代替之
# import types
#
# if type(num) == types.IntType:
#     pass
#
# #对象身份比较优于对象值比较
# #值比较：
# if type(num) == type(0):
#     pass
# #对象身份比较：
# if type(num) is types.IntType:
#     pass
#
# #减少查询次数
# #import types
# from types import IntType
# if type(num) is IntType:
#     pass
#
# #惯例风格可读性的考虑：使用isinstance()
#
#
# 最终代码
def displayNumType(num):
    print num ,'is',
    #isinstance同时判断多个种类的用法
    #如果是这四个其中之一
    if isinstance(num,(int, long, float, complex)):
        #返回这个type的名字
        print 'a number of type:', type(num).__name__
    else:
        print 'not a number at all!!'

displayNumType(-69)
displayNumType(9999999999999999999999999L)
displayNumType(98.6)
displayNumType(-5.2+1.9j)
displayNumType('xxx')

