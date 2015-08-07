#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xy'

import hashlib


def gethash(f):
    line = f.readline()
    hash = hashlib.md5()
    while(line):
        hash.update(line)
        line = f.readline()
    return hash.hexdigest()


def is_hash_equal(f1, f2):
    str1 = gethash(f1)
    str2 = gethash(f2)
    return str1 == str2

if __name__ == '__main__':
    f1 = open("./a_.txt", "r")
    f2 = open("./a__.txt", "r")
    if is_hash_equal(f1, f2):
        print 'same!'
    else:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        for i in range(min(len(lines1), len(lines2))):
            if lines1[i] != lines2[i]:
                print i
                break


'''
compare two files' MD5 value
'''