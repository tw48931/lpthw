#-*-coding: utf-8 -*-

f=open('123.txt')
g=open('to.txt','w')

try:
    while True:
        line=f.readline()
        if len(line)==0:
            break
        if line.count('\n')==len(line):
            continue
        g.write(line)

finally:
    f.close()
    g.close()