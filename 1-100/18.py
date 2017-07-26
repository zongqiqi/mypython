"""求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。"""

a = int(input("please input a digit"))
b = int(input("how many?"))
l=[]
n0 = 0
for i in range(b):
	n = a*(10**i)
	n0 = n0+n
	l.append(n0)
print (l)
print (sum(i for i in l))
