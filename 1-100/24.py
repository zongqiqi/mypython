"""有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。"""

def fabi(n):
    x,y=0,1
    for a in range(1,n+1):
        x,y=y,x+y
    return y
s= 0
for a in range(1,21):
    x = fabi(a+1)/fabi(a)
    s+=x
    print (x)
print (s)


