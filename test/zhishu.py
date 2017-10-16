def getprim(n):
    p=2
    x=0
    while(x<n):
        result=True
        for i in range(2,p-1):
            if(p%i==0):
                result=False#如果P能被任意一个小于n的数整除，则非质数
        if result==True:
            print(p) #如果是质数，则打印
            x=x+1#计数+1
        p+=1#P+1

getprim(522048)