"""一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。"""
l = []
for i in range(1,1000):
    sum = 0
    for a in range(1,i):
        if i%a==0:
            sum =sum+a
    if i == sum:
        l.append(i)
print (l)     


