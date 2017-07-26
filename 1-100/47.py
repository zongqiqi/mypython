"""两个变量值互换。"""

def exchange(a,b):
    a,b=b,a
    return a,b


a= input('aaaaa')
b=input('bbbbbbb')
if __name__ == '__main__':
    print('a= %s,b= %s'%(a,b))
    a,b=exchange(a,b)
    print('a= %s,b= %s'%(a,b))
