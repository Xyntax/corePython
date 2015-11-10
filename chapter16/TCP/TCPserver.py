#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xy'

"""
TCP时间戳服务器
"""

"""
改制poetry的测试结果

1.阻塞(block).

    这个TCP服务器程序运行时，先后使用两次nc localhost port连接。
    在第一首诗歌没有发送完成时，阻塞。直到data ends，
    与第一个断开连接之后，才开始第二个连接发送。

    waiting for connection
    ('... connected from:', ('127.0.0.1', 41354))
    data ends
    waiting for connection
    ('... connected from:', ('127.0.0.1', 41379))

2.对于客户端连接的检测.

    tcpClisock, addr = tcpSocket.accept()
    这个函数会自身循环，一直到有客户端接入，将两个结果return之后，才进行下一句。
    所以这个检测客户端接入的过程不需要程序员手动写。

3.TODO.

    程序ctrl-c之后无法自动回收端口
    客户端断开之后，socket.error: [Errno 32] Broken pipe

4.源程序改进(twisted/tw-into/block-server/slowpoetry)

    main()中进行args的读取和socket的初始化，调用serve()完成工作
    一、把两层while的外层while做成serve()函数
        函数功能：
        1 判断接入并获取接入信息tcpSocket.accept()
        2 调用send_poetry()函数发送数据
    二、把内层函数抽象成发送诗歌信息的函数send_poetry()

"""

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSocket = socket(AF_INET, SOCK_STREAM)
tcpSocket.bind(ADDR)
tcpSocket.listen(5)

while True:
    print('waiting for connection')
    tcpClisock, addr = tcpSocket.accept()
    print('... connected from:', addr)

    while True:
        data = tcpClisock.recv(BUFSIZ)
        if not data:
            break
        tcpClisock.send('[%s] %s' % (ctime(), data))
        tcpClisock.close()

tcpSocket.close()
