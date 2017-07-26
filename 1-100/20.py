"""一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？"""
a = 100
b =50
l = []
for i in range(1,11):
    b = a/2
    l.append(a)
    a = b
    l.append(a)
print ('共经历了%s' %(sum(cc for cc in l[:-2])))
print ('第十次高为%s' %(l[-1]))
print(l)



