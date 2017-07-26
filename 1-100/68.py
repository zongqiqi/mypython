"""有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数"""
n=10
m=3
l=[]
for i in range(n):
    l.append(i)
print(l)
l1 =l[-m:]
l2 =l[:-m]  
l4 = l1+l2
print (l4)

