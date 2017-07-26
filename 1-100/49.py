"""使用lambda来创建匿名函数。"""

maxmum = lambda x,y:(x>y)*x+(x<y)*y
minmum = lambda x,y:(x>y)*y+(x<y)*x

if __name__=='__main__':
    a = 10
    b=20
    print ('The larger one is %d'%maxmum(a,b))
    print('The lowerr one is %d'%minmum(a,b))



