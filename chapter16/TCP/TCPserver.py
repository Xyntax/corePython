#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'xy'

"""
TCP时间戳服务器
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
