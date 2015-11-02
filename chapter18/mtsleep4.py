# -*- coding: utf-8 -*-
__author__ = 'xy'

# !/usr/bin/env python

import threading
from time import sleep, ctime

loops = [4, 2]


class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        # apply(self.func, self.args)
        self.res = self.func(*self.args)


def loop(nloop, nsec):

    '''ctime() -> Jun 25 21:46:01 2015'''
    print('start loop', nloop, 'at:', ctime())

    sleep(nsec)

    print('loop', nloop, 'done at:', ctime())


def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:

        # init thread with function and args
        # 传入一个类
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    # start threads
    for i in nloops:
        threads[i].start()

    # wait for all threads to finish
    for i in nloops:
        # 主线程会等待所有join()的线程结束
        # join()在给了timeout会等到超时停止
        threads[i].join()

    print('all Done at:', ctime())

if __name__ == '__main__':
    main()

'''
starting at: Thu Jun 25 22:03:13 2015
start loop 0 at: Thu Jun 25 22:03:13 2015
start loop 1 at: Thu Jun 25 22:03:13 2015
loop 1 done at: Thu Jun 25 22:03:15 2015
loop 0 done at: Thu Jun 25 22:03:17 2015
all Done at: Thu Jun 25 22:03:17 2015
'''