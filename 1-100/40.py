"""将一个数组逆序输出"""
import random
l=[]
for a in range(10):
    l.append(int(random.random()*100))
print(l)

for b in range(len(l)):
    print(l[-(b+1)],'  ',end='')

print('')
for c in l[::-1]:
    print (c,'  ',end='')
