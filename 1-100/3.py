from math import sqrt

for x in range(0,100000000):
    a=sqrt(x+100)
    if a%1==0 :
        b=sqrt(x+168)
        if b%1==0 :
            print (a,b,x);
            break
