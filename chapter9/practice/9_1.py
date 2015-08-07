#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xy'

file = raw_input('enter file path')
fobj = open(file, 'r')
i = 0
for eachline in fobj:
    if eachline.strip(' ')[0] != '#':
        # if not eachline.startswith('#')
        i += 1
print i

'''
try to use startswith() and endswith()

'''