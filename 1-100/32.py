"""按相反的顺序输出列表的值。"""


a = ['one', 'two', 'three']

for i in range(1,len(a)+1):
    print(a[-i])



for b in a[::-1]:
    print (b)
