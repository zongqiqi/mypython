"""有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。"""

l=[1,2,3,4,5,7,8,9]
l.insert(0,6)
print(l)

for a in range(len(l)-1):
    if l[a]>l[a+1]:
        l[a],l[a+1]=l[a+1],l[a]

print(l)
