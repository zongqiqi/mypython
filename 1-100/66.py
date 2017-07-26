"""输入3个数a,b,c，按大小顺序输出。"""

import random
l=[] 
for a in range(3):
    l.append(int(random.random()*100))
print(l)
for b in range(len(l)):
    for c in range(b,len(l)):
        if l[b]>l[c]:
            l[b],l[c]=l[c],l[b]
print(l)




