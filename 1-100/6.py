#0,1,1,2,3,5,8....



def f(cc):
    x,y=0,1
    ff=[0,1]
    for i in range(0,cc-2):
        x,y =y, x+y
        print (y)
        ff.append(y)
    return ff
a=int(input())
ff = f(a)
print (ff)


