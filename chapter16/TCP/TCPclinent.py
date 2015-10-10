#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xy'

"""
TCP 客户端
优雅退出：把while循环放到try-catch中，捕获EOF error和Keyinterrupt error，在except写close()
"""

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data)

tcpCliSock.close()
