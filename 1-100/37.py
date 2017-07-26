"""对10个数进行排序。"""
import random

l=[]
for b in range(10):
    l.append(int(random.random()*100))
print (l)
for a in range(len(l)):
    for b in range(a+1,len(l)):
        if l[a]>l[b]:
            l[a],l[b]=l[b],l[a] 

print (l)
