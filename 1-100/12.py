import math
m=range(101,201)
p=list(m[:])
for i in range(101,201):
    for j in range(2,i-1):
        if i % j == 0:
            p.remove(i)
            break
print(p)
print("101至200之间的素数一共有%d个"%len(p))
