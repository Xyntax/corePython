'''
edit by xy


'''

# -*- coding: utf-8 -*-

def foo(debug = True):
    '函数的默认参数'
    if debug:
        print 'in debug mode'

    print 'done'

foo()

foo(False)


