# -*- coding: utf-8 -*-
__author__ = 'xy'

import string

alphas = string.letters + '_'
nums = string.digits

myInput = raw_input('Identifier to test:(len>=2)\n')

# if len(myInput) > 1:
#     if myInput[0] not in alphas:
#         print 'invalid'
#     else:

##for-else：else中的语句，在for完整的循环完而且没有遇到break的时候才执行

#         for otherChar in myInput[1:]:
#             if otherChar not in alphas + nums:
#                 print 'invalid'
#                 break
#         else:
#             print 'ok,pass!'

#性能考虑：减少函数调用次数、减少操作和运算次数——>将结果保存为变量

if len(myInput) > 1:
    if myInput[0] not in alphas:
        print 'invalid'
    else:

        #优化：将变量保存，减少循环中的调用次数
        s = myInput[1:]
        ss = alphas + nums

        for otherChar in s:
            if otherChar not in ss:
                print 'invalid'
                break
        else:
            print 'ok,pass!'
