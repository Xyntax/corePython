#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'xy'

from socket import *
from time import ctime

HOST = ''
PORT = 21568
ADDR = (HOST, PORT)
BUFFSIZE = 1024

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waiting for message...')
    data, addr = udpSerSock.recvfrom(BUFFSIZE)
    udpSerSock.sendto('[%s] %s' % (ctime(), data), addr)
    print('...received from and returned to: ', addr)

udpSerSock.close()
