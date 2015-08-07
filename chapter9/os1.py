__author__ = 'xy'

import os1

'''
os
linesep
sep
pathsep
curdir
pardir
'''
filename = raw_input('Enter file name') # raw_input 不会保留输入时的换行符
fobj = open(filename, 'w')
while True:
    aLine = raw_input("Enter a line ('.' to quit)")
    if aLine != '.':
        fobj.write('%s%s' % (aLine, os1.linesep)) # 表示换行符
    else:
        break
fobj.close()
