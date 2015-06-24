'''
edit by xy


'''

# -*- coding: utf-8 -*-

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


