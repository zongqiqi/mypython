#coding: utf-8
"""有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？"""
d=[]
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
        	if ( i != j ) and ( j != k ) and ( i != k):
        		d.append([i,j,k])
print ('总数量为',len(d));        		
print (d);
