foo='abc'

for i in range(len(foo)):#range+len按长度遍历字符串
    print foo[i]+ '(%d)' % i  ,#','表示用空格替换换行
