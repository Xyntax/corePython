#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xy'

import os


file1 = raw_input("please enter the file:")
with open(file1) as fobj1:  # 打开源文件
    with open("temp.txt", "w") as fobj2:  # 打开临时文件
        for i in fobj1:  # 按行遍历源文件
            if len(i) > 80:  # 如果字符串长度大于80
                num = list(i)
                count = len(num) / 80
                for k in range(count):
                    fobj2.write("".join(num[:79]))
                    fobj2.write("\n")
                    num = num[79:]
                    fobj2.write("".join(num))
            else:
                fobj2.write(i)
                fobj2.write("\n")
                with open("temp.txt") as f2:
                    with open(file1, "w") as f1:
                        for j in f2:
                            f1.write(j)
os.remove('temp.txt')