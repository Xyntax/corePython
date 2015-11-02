# !/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'xy'
import ftplib
import os
import socket

HOST = 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'


def main():
    # 连接
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror), e:
        print('ERROR: cannot connect "%s"' % HOST)
        return
    print('*** Connected to host "%s" ***' % HOST)
    # 登录（匿名）
    try:
        f.login()
    except ftplib.error_perm:
        print('ERROR: cannot login as anonymous')
        f.quit()
        return
    print('*** Logged in as anonymous ***')
    # 目录切换
    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print('ERROR: cannot cwd to "%s"' % DIRN)
        f.quit()
        return
    print('*** Changed to "%s" folder ***' % DIRN)
    # 下载文件
    try:
        f.retrbinary('RETR %s' % FILE,
                     open(FILE, "wb").write())
    except ftplib.error_perm:
        print('ERROR: cannot read file "%s"' % FILE)
        os.unlink(FILE)
    else:
        print('Download "%s" to CWD' % FILE)
    f.quit()
    return


if __name__ == "__main__":
    main()
