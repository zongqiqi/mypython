"""输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。"""
import random
l=[] 
for a in range(10):
    l.append(int(random.random()*100))
print(l)
nMax=max( a for a in l )
nMin=min(a for a in l )
print("max=",nMax,"min=",nMin)
l.remove(nMax)
l.remove(nMin)
l.insert(0,nMax)
l.append(nMin)
print(l)



