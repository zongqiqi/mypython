"""利用递归方法求5!。"""
try:
    n = int(input("输入一个数字"))
except:
    n=int(input("数字!!!!!!!!!"))
if n<0:
    n=int(input("正整数"))#############这里有问题
else:
    def faunc(n):
        if n == 1 or n ==0:
            return 1
        else:
            return faunc(n-1)*n
print( faunc(n))



