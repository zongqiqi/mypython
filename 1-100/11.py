
"""有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？"""
def fabi(n):
	x=1
	y=1
	if n<3:
		z = 1
	else:
		for i in range(1,n-1):
			x,y=y,x+y
	print (y)
	return y

number = int(input())
fabi(number)

