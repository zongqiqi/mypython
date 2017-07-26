"""列表排序及连接。"""
l1=[1,2,3]
l2=[4,5,6]
l=l2+l1
print(l)
l.sort()
print (l)
l.extend(l1)
print(l)
