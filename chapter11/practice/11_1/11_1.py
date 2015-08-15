#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xy'


def countToFour1():
    for eachNum in range(5):
        print(eachNum)


def countToFour2(n):
    for eachNum in range(n, 5):
        print(eachNum)


def countToFour3(n=1):
    for eachNum in range(n, 5):
        print(eachNum)


a = 2
b = 4
c = 5

d = max(1,2,3)
# countToFour1(a) error
countToFour2(a)
countToFour3(a)

# countToFour1(b) error
countToFour2(b)
countToFour3(b)

# countToFour1(c) error
countToFour2(c)
countToFour3(c)

countToFour1()
# countToFour2() error
countToFour3()
