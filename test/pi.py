#-*- coding:utf-8 -*-
def pi(places=10):
    """Computes pi to given number of decimal places
      参数places表示要返回的pi的小数点后位数  
      方法：先整体扩大10**8（10的八次方）倍，然后计算完成后再缩小10的八次方倍
    """
     
    # 3 + 3*(1/24) + 3*(1/24)*(9/80) + 3*(1/24)*(9/80)*(25/168)
    # The numerators 1, 9, 25, ... are given by (2x + 1) ^ 2
    # The denominators 24, 80, 168 are given by (16x^2 -24x + 8)
    extra = 8
    one = 10 ** (places+extra)
    t, c, n, na, d, da = 3*one, 3*one, 1, 0, 0, 24
    #这里的n 和d 分别为每一项的分子与分母 ,na 和 da 分别为分子和分分母后一项比前一项增加的数值
    #这里的//可不是C++中的注释,而是除的意思
    while t > 1: 
        n, na, d, da = n+na, na+8, d+da, da+32
        t = t * n // d
        c += t
    return c // (10 ** extra)
print(pi(10000))
