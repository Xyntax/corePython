'''
edit by xy


'''

# -*- coding: utf-8 -*-

try:
    filename = raw_input('Enter file name')
    fobj = open(filename,'r')

    for eachline in obj :
        print eachline

    fobj.close()

except IOError,e:
    print 'file open error:', e
