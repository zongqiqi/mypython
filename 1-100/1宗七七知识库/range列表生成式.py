"""列表生成式"""

for x in range(1, 11):#序列

[x * x for x in range(1, 11)]#列表生成

[x * x for x in range(1, 11) if x % 2 == 0]#列表生成+条件

[m + n for m in 'ABC' for n in 'XYZ']#列表生成+两层循环

[k + '=' + v for k, v in d.iteritems()]#列表提取

[s.lower() for s in L]#列表生成
