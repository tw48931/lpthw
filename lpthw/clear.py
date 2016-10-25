#-*- coding :utf-8 -*-                 

file = open('123.txt')

i = 0
while 1:
    line = file.readline().strip()
    if not line:
        break
    i = i + 1
    line1 = line.replace('\r','')
    f1 = open('E:/guochanqixie1.txt','a')
    f1.write(line1 + '\n')
    f1.close()
print str(i)
