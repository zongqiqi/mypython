"""变量作用域"""

num = 2
def autofunc():
    num = 1
    print ('Internal block num=%d'%num)
    num+=1

for i in range(3):
    print('Number =%d'%num)
    num+=1
    autofunc()

