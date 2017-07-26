"""求一个3*3矩阵对角线元素之和。"""

import random
n = 3
l = []
s =0
for a in range(n):
    l1=[]
    for b in range(n):
        i = int(random.random()*10)
        l1.append(i)
    l.append(l1)
print(l)

for c in range(n):
    s = l[c-1][c-1]+l[c-1][-c]+s
if n%2!=0:
    s = s-l[int((n+1)/2)-1][int((n+1)/2-1)]
    print(l[int((n+1)/2)-1][int((n+1)/2)-1])
print (s)
