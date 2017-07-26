"""求100之内的素数。"""
l = [x for x in range(1,100)]
for a in range(1,100):
    for b in range(2,a):
        if a%b ==0:
            l.remove(a)
            break
print (l)
        


