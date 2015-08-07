#!/usr/bin/env python

import os1
for tmpdir in ('/tmp', r'c:\temp'):
    if os1.path.isdir(tmpdir):
        break

else:
    print 'no temp directory available'
    tmpdir = ''

if tmpdir:
    os1.chdir(tmpdir)
    cwd = os1.getcwd()
    print '*** current temporatory directory'
    print cwd

    print '*** creating example directory'
    os1.mkdir('example')
    os1.chdir('example')
    cwd = os1.getcwd()
    print '*** new working directory:'
    print cwd
    print '*** original directory listing:'
    print os1.listdir(cwd)
