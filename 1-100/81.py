"""809*??=800*??+9*??+1 其中??代表的两位数,8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果。"""

for a in range(10,100):
    if a*8<100 and 9*a>=100 and 809*a==800*a+9*a+1:
        print ('a=',a,'809*a',809*a)



