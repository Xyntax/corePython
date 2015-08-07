file_object = open(file_name, access_mode = 'r', buffering = -1)
'''
file_name:绝对路径或者相对路径
access mode:
r read
w write
a add
U 通用换行符支持
其中w打开时清空
r U必须打开已存在文件
a = fopen()
+ 读写
b 二进制
'''
fp = open('/etc/motd')
fp = open('test', 'w')
fp = open('data', 'r+')
fp = open(r'c:\io.sys', 'rb')

file

if isinstance(f, file)

# 处理换行符
f = open('myfile', 'r')
data = [line.strip() for line in f.readlines()]
f.close()

seek()
text()


# 文件迭代(包括换行符)
for eachline in f:

# 读取全文后再打印
filename = raw_input('Enter file name')
f = open(filename, 'r')
allLines = f.readlines()
f.close()                               # 位置
for eachline in allLines:
    print eachline

# 读取一行打印一行
filename = raw_input('Enter file name')
f = open(filename, 'r')
for eachline in f:
    print eachline
f.close()                               # 位置