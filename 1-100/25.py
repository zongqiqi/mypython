"""求1+2!+3!+...+20!的和。"""
s=0
for a in range(1,21):
    c=1
    for b in range(1,a+1):
        c=c*b
    s+=c
    print(a,"   ",c)
print(s)



