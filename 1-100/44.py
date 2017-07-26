"""两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵"""
import random


def arr(n):
    l=[]
    for a in range(n):
        l1=[]
        for b in range(n):
            ccc = int(random.random()*100)
            l1.append(ccc)
        l.append(l1)
    return l
a1=arr(3)
a2=arr(3)
print (a1)
print (a2)
a3 = []
for a in range(len(a1)):
    l3 = []
    for b in range(len(a1[a])):
        l3.append(a1[a][b]+a2[a][b])
    a3.append(l3)
print (a3)

