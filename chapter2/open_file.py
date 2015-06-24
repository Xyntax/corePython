'''
edit by xy


'''

# -*- coding: utf-8 -*-

filename = raw_input('Enter file name:')

fobj = open(filename,'r')#r,w,a,+,b

for eachline in fobj:
    print eachline

fobj.close()

