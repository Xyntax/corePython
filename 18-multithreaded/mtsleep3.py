#!/usr/bin/env python

import threading
from time import sleep, ctime

loops = [4, 2]


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
        t = threading.Thread(target=loop, args=(i, loops[i]))
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
