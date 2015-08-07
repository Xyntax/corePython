#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xy'

def print_25_lines(file):
    num = 0
    for eachline in file:
        if num == 25:
            raw_input('press any key to continue')
            print_25_lines(file[25:])
        else:
            print eachline
            num += 1

file_list = open('./test_100lines.txt', 'r').readlines()
print_25_lines(file_list)

'''
with open("test_100lines.txt","a+") as fobj:

    for i in range(100):

        fobj.write(str(i))

        fobj.write("\n")
'''