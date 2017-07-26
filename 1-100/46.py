"""求输入数字的平方，如果平方运算后小于 50 则退出。"""

mark=1
while mark:
    try:
        a =int(input('a number'))
    except:
        pass
    print(a**2)
    if a**2<50:
        mark = 0

