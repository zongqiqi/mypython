"""利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。"""

s= input('input \n')
n = len(s)
def a(s,n):
    if n-1>0:
        print (s[n-1])
        a(s,n-1)
a(s,n)
