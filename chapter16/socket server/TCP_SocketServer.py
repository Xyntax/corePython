#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'xy'

from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21569
ADDR = (HOST, PORT)


class MyRequestHandler(SRH):
    def handle(self):
        print('...connected from: ', self.client_address)
        self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))


tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting for connection...')
tcpServ.serve_forever()
